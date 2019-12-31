from manimlib.scene.scene import Scene
from manimlib.constants import *
import copy
from manimlib.web.utils import (
    animation_to_json,
    wait_to_json,
    scene_mobjects_to_json,
    mobject_to_json,
    serialize_scene,
    scene_diff,
    update_initial_mobject_serializations,
    update_current_mobject_serializations,
)
from manimlib.mobject.mobject import Mobject, Group
from manimlib.mobject.svg.tex_mobject import (
    TexMobject,
    TextMobject,
    SingleStringTexMobject,
)
from collections import defaultdict


class WebScene(Scene):
    def __init__(self, **kwargs):
        self.scene_diffs = []
        self.animation_diffs = []
        self.initial_mobject_serializations = {}
        self.last_scene = []
        self.current_mobject_serializations = {}

        # A list of snapshots of the Scene before each Animation
        self.scenes_before_animation = []
        # A list of serialized Animations
        self.animation_list = []
        self.render_kwargs = kwargs
        # A mapping of IDs to Mobjects
        self.initial_mobject_dict = {}

    def render(self):
        # Regular Scenes render upon instantiation.
        super(WebScene, self).__init__(**self.render_kwargs)
        self.name_initial_mobjects()

    # TODO: Rather than computing diffs between scenes, use the
    # current_mobject_serializations dict.
    def play(self, *args, **kwargs):
        animation = args[0]

        # Compute scene diff
        self.initial_mobject_serializations = update_initial_mobject_serializations(
            self,
            self.initial_mobject_serializations,
            # In case a Mobject being added by the Animation hasn't been seen before.
            animation=animation,
        )
        cur_scene = serialize_scene(self)
        self.scene_diffs.append(
            scene_diff(
                self.last_scene,
                cur_scene,
                self.current_mobject_serializations,
            )
        )
        self.current_mobject_serializations = update_current_mobject_serializations(
            cur_scene,
            self.current_mobject_serializations,
        )
        self.last_scene = cur_scene


        if animation.__class__.__name__.startswith("ApplyPointwiseFunction"):
            self.update_initial_mobject_dict(mobject_list=[animation.mobject])
        else:
            self.update_initial_mobject_dict(mobject_list=animation.get_args())
        self.scenes_before_animation.append(scene_mobjects_to_json(self.mobjects))
        self.animation_list.append(animation_to_json(args, kwargs))
        super(WebScene, self).play(*args, **kwargs)


        # Compute animation diff
        self.initial_mobject_serializations = update_initial_mobject_serializations(self, self.initial_mobject_serializations)
        cur_scene = serialize_scene(self)
        self.animation_diffs.append(
            scene_diff(
                self.last_scene,
                cur_scene,
                self.current_mobject_serializations,
                animation=animation,
                scene_diff=self.scene_diffs[len(self.scene_diffs) - 1],
            )
        )
        self.current_mobject_serializations = update_current_mobject_serializations(
            cur_scene,
            self.current_mobject_serializations
        )
        self.last_scene = cur_scene


    def wait(self, duration=DEFAULT_WAIT_TIME, stop_condition=None):
        self.scenes_before_animation.append(scene_mobjects_to_json(self.mobjects))
        self.animation_list.append(wait_to_json(duration, stop_condition))
        super(WebScene, self).wait(duration=duration, stop_condition=stop_condition)

    def update_initial_mobject_dict(self, mobject_list=None, include_self=True):
        mob_list = [] if mobject_list is None else list(mobject_list)
        if include_self:
            mob_list += self.mobjects
        for mob in mob_list:
            mob_id = id(mob)
            if mob_id not in self.initial_mobject_dict:
                self.initial_mobject_dict[mob_id] = mobject_to_json(mob)
                if type(mob) in [
                    Group,
                    Mobject,
                    TexMobject,
                    TextMobject,
                    SingleStringTexMobject,
                ]:
                    # handle the submobjects
                    self.update_initial_mobject_dict(mobject_list=mob.submobjects, include_self=False)

    def name_mobject_serialization(self, serialization, id_to_name, class_to_number):
        new_serialization = {}
        for k, v in serialization.items():
            if k == "id":
                continue
            elif k == "submobjects":
                new_submobjects = []
                for child_serialization in v:
                    child_name = name_from_serialization(child_serialization, id_to_name, class_to_number)
                    new_serialization[self.name_from_serialization(serialization, id_to_name, class_to_number)] = \
                        self.name_from_serialization(child_serialization, id_to_name, class_to_number)
            else:
                new_serialization[k] = v
        return new_serialization


    def name_from_serialization(self, serialization, id_to_name, class_to_number):
        mobject_id = serialization["id"]
        if mobject_id in id_to_name:
            return id_to_name[mobject_id]
        else:
            mobject_class = serialization["className"]
            class_number = class_to_number[mobject_class] + 1
            class_to_number[mobject_class] += 1
            serialization_name = f"{mobject_class}{class_number}"
            id_to_name[mobject_id] = serialization_name
        return serialization_name


    def name_initial_mobjects(self):
        new_initial_mobjects = {}
        id_to_name = defaultdict(str)
        class_to_number = defaultdict(int)
        for parent_mobject_serialization in self.initial_mobject_dict:
            name = name_from_serialization(parent_mobject_serialization)
            new_initial_mobjects[name] = name_mobject_serialization(parent_mobject_serialization, id_to_name, class_to_number)
        return new_initial_mobjects


    def tear_down(self):
        # convert scenes_before_animation to diffs?
        pass
