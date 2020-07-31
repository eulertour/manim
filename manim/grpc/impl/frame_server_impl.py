from concurrent import futures
import grpc
import threading
import subprocess as sp
import dill
from google.protobuf import json_format
from ..gen import frameserver_pb2
from ..gen import frameserver_pb2_grpc
from ...scene import scene
from ..gen import renderserver_pb2
from ..gen import renderserver_pb2_grpc
from ...config import camera_config


class FrameServer(frameserver_pb2_grpc.FrameServerServicer):
    def __init__(self, scene_class):
        self.keyframes = []
        self.scene = scene_class(frame_server=self)
        self.scene_thread = threading.Thread(
            target=lambda s: s.render(), args=(self.scene,)
        )
        self.scene_thread.start()
        self.previous_frame_animation_index = None
        self.scene_finished = False

        # If a javascript renderer is running, notify it of the scene
        # being served. If not, spawn one.
        with grpc.insecure_channel("localhost:50052") as channel:
            stub = renderserver_pb2_grpc.RenderServerStub(channel)
            try:
                request = renderserver_pb2.ManimStatusRequest(
                    scene_name=str(self.scene)
                )
                stub.ManimStatus(request)
            except grpc._channel._InactiveRpcError:
                sp.Popen(camera_config["js_renderer_path"])

    def GetFrameAtTime(self, request, context):
        # Update the Scene to the requested time.
        time = request.animation_offset
        current_frame_animation_index = request.animation_index

        if request.animation_index >= len(self.keyframes):
            raise NotImplementedError("Implement a way to skip forward")
        elif request.animation_index < len(self.keyframes) - 1:
            selected_scene = self.keyframes[request.animation_index]
        else:
            selected_scene = self.scene

        # play() uses run_time and wait() uses duration.
        duration = (
            selected_scene.run_time
            if selected_scene.animations
            else selected_scene.duration
        )

        animation_finished = False
        if time > duration:
            if request.animation_index == len(self.keyframes) - 1:
                # Ensure that self.scene will notify the renderer when the next
                # animation is ready.
                selected_scene.renderer_waiting = True

                # Signal self.scene to continue to the next animation.
                selected_scene.animation_finished.set()

                # Notify the renderer that the current animation is finished.
                return frameserver_pb2.FrameResponse(
                    frame_pending=True, scene_finished=self.scene_finished,
                )
            else:
                assert request.animation_index < len(self.keyframes) - 1
                animation_finished = True
                time -= duration
                selected_scene = self.keyframes[request.animation_index + 1]
                current_frame_animation_index = request.animation_index + 1

        if not hasattr(selected_scene, "camera"):
            setattr(selected_scene, "camera", self.scene.camera)

        if selected_scene.animations:
            # This is a call to play().
            selected_scene.update_animation_to_time(time)
            selected_scene.update_frame(
                selected_scene.moving_mobjects,
                selected_scene.static_image,
                selected_scene.static_image_serialization,
            )
            serialized_mobject_list, duration = selected_scene.add_frames(
                *selected_scene.get_frame()
            )
            resp = list_to_frame_response(serialized_mobject_list, duration)
            if current_frame_animation_index != self.previous_frame_animation_index:
                self.previous_frame_animation_index = current_frame_animation_index
                resp.duration = selected_scene.run_time
                if len(selected_scene.animations) == 1:
                    resp.animation_name = str(selected_scene.animations[0])
                else:
                    resp.animation_name = f"{str(selected_scene.animations[0])}..."
            resp.animation_finished = animation_finished
            return resp
        else:
            # This is a call to wait().
            if selected_scene.should_update_mobjects():
                # TODO, be smart about setting a static image
                # the same way Scene.play does
                selected_scene.update_animation_to_time(time)
                selected_scene.update_frame()
                serialized_mobject_list, duration = selected_scene.add_frames(
                    *selected_scene.get_frame()
                )
                frame_response = list_to_frame_response(
                    serialized_mobject_list, duration
                )
                if (
                    selected_scene.stop_condition is not None
                    and selected_scene.stop_condition()
                ):
                    selected_scene.animation_finished.set()
                    frame_response.frame_pending = True
                    selected_scene.renderer_waiting = True
                return frame_response
            elif selected_scene.skip_animations:
                # Do nothing
                return
            else:
                selected_scene.update_frame()
                dt = 1 / selected_scene.camera.frame_rate
                serialized_mobject_list, duration = selected_scene.add_frames(
                    *selected_scene.get_frame(),
                    num_frames=int(selected_scene.duration / dt),
                )
                resp = list_to_frame_response(
                    serialized_mobject_list, selected_scene.duration
                )
                if current_frame_animation_index != self.previous_frame_animation_index:
                    self.previous_frame_animation_index = current_frame_animation_index
                    resp.animation_name = "Wait"
                resp.animation_finished = animation_finished
                return resp

    def RendererStatus(self, request, context):
        response = frameserver_pb2.RendererStatusResponse()
        response.scene_name = str(self.scene)
        return response

    def UpdateSceneLocation(self, request, context):
        response = frameserver_pb2.SceneLocationResponse()
        return response


def list_to_frame_response(serialized_mobject_list, duration):
    response = frameserver_pb2.FrameResponse()
    response.frame_pending = False
    response.duration = duration
    for mob_serialization in serialized_mobject_list:
        mob_proto = response.mobjects.add()
        mob_proto.id = mob_serialization["id"]
        mob_proto.needs_redraw = mob_serialization["needs_redraw"]
        for point in mob_serialization["points"]:
            point_proto = mob_proto.points.add()
            point_proto.x = point[0]
            point_proto.y = point[1]
            point_proto.z = point[2]
        mob_proto.style.fill_color = mob_serialization["style"]["fill_color"]
        mob_proto.style.fill_opacity = float(mob_serialization["style"]["fill_opacity"])
        mob_proto.style.stroke_color = mob_serialization["style"]["stroke_color"]
        mob_proto.style.stroke_opacity = float(
            mob_serialization["style"]["stroke_opacity"]
        )
        mob_proto.style.stroke_width = float(mob_serialization["style"]["stroke_width"])
    return response


def get(scene_class):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    frameserver_pb2_grpc.add_FrameServerServicer_to_server(
        FrameServer(scene_class), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    return server
