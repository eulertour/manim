import sys
import numpy as np
if sys.platform == "emscripten":
    import js
    import pyodide
else:
    from manimlib.web.web_mock import tex2points

def serialize_arg(arg):
    from manimlib.mobject.mobject import Mobject
    if isinstance(arg, Mobject):
        return id(arg)
    else:
        return arg

def serialize_args(args):
    return [serialize_arg(arg) for arg in args]

def serialize_config(config):
    return { k: serialize_arg(v) for (k, v) in config.items() }

def serialize_scene(scene):
    ret = []
    for mob in scene.mobjects:
        ret.append(serialize_mobject(mob))
    return ret

SUBMOBJECT_IGNORE_LIST = ["SingleStringTexMobject"]

def serialize_mobject(mob):
    from manimlib.mobject.mobject import Group, Mobject
    from manimlib.mobject.types.vectorized_mobject import VMobject, VGroup
    class_name = mob.__class__.__name__
    ret = {
        "id": id(mob),
        "className": class_name,
        "args": mob.args,
        "config": mob.config,
        "submobjects": [serialize_mobject(mob) for mob in mob.submobjects if class_name not in SUBMOBJECT_IGNORE_LIST],
        "transformations": mob.transformations,
    }
    if isinstance(mob, VMobject):
        ret["position"] = mob.get_center()
        ret["style"] = get_mobject_style(mob)
    return ret

def serialize_animation(animation):
    return {
        "className": animation.__class__.__name__,
        "args": animation.args,
        "config": animation.config,
    }

def scene_diff(
    starting_scene,
    ending_scene,
    mobject_serializations,
    animation=None,
    scene_diff=None,
):
    ret = {}
    if animation is not None:
        ret["animation"] = serialize_animation(animation)
    for starting_mobject_serialization in starting_scene:
        # Search for the Mobject in the ending scene.
        starting_mobject_id = starting_mobject_serialization["id"]
        starting_mobject_in_ending_scene = False
        for ending_mobject_serialization in ending_scene:
            if ending_mobject_serialization["id"] == starting_mobject_id:
                # Add the diff if the Mobject was changed.
                diff = mobject_serialization_diff(starting_mobject_serialization, ending_mobject_serialization)
                if diff != {}:
                    ret[starting_mobject_id] = diff
                starting_mobject_in_ending_scene = True
                break
        # Mark the Mobject as removed if it isn't in the ending scene.
        if not starting_mobject_in_ending_scene:
            ret[starting_mobject_id] = {"removed": True}
    # Check for Mobjects that were added.
    for ending_mobject_serialization in ending_scene:
        ending_mobject_id = ending_mobject_serialization["id"]
        if not any(serialization["id"] == ending_mobject_id for serialization in starting_scene):
            if ending_mobject_id in mobject_serializations:
                # This Mobject has been added before, so save its diff to the
                # scene_diff in case it was changed offscreen.
                added_mobject_diff = mobject_serialization_diff(
                    mobject_serializations[ending_mobject_id],
                    ending_mobject_serialization,
                )
                if scene_diff is None:
                    added_mobject_diff["added"] = True
                    ret[ending_mobject_id] = added_mobject_diff
                else:
                    ret[ending_mobject_id] = {"added": True}
                    scene_diff[ending_mobject_id] = added_mobject_diff
            else:
                ret[ending_mobject_id] = {"added": True}

    return ret

# TODO: When a submobject is added, check for offscreen updates.
def mobject_serialization_diff(starting_serialization, ending_serialization):
    ret = {}
    for attr in starting_serialization:
        if attr == "submobjects":
            submobjects_diff = []
            starting_submobject_ids = list(map(lambda serialization: serialization["id"], starting_serialization["submobjects"]))
            ending_submobject_ids = list(map(lambda serialization: serialization["id"], ending_serialization["submobjects"]))
            newly_added_ids = [id for id in ending_submobject_ids if id not in starting_submobject_ids]
            newly_removed_ids = [id for id in starting_submobject_ids if id not in ending_submobject_ids]
            persisting_ids = [id for id in starting_submobject_ids if id in ending_submobject_ids]
            for id in newly_added_ids:
                submobjects_diff.append({id: {"added": True}})
            for id in newly_removed_ids:
                submobjects_diff.append({id: {"removed": True}})
            for id in persisting_ids:
                starting_submobject_serialization = None
                ending_submobject_serialization = None
                for serialization in starting_serialization["submobjects"]:
                    if serialization["id"] == id:
                        starting_submobject_serialization = serialization
                for serialization in ending_serialization["submobjects"]:
                    if serialization["id"] == id:
                        ending_submobject_serialization = serialization
                diff = mobject_serialization_diff(starting_submobject_serialization, ending_submobject_serialization)
                if diff:
                    submobjects_diff.append({id: diff})
            if submobjects_diff:
                ret["submobjects"] = submobjects_diff
        else:
            starting_attr = starting_serialization[attr]
            ending_attr = ending_serialization[attr]
            if attr == "position":
                if not np.array_equal(starting_attr, ending_attr):
                    ret["position"] = (starting_attr, ending_attr)
            else:
                if starting_attr != ending_attr:
                    ret[attr] = (starting_serialization[attr], ending_serialization[attr])
    return ret

# TODO: Compare with default Mobject to compute changes prior to adding.
def update_initial_mobject_serializations(scene, mobject_serializations, animation=None):
    mobjects = []
    if animation is not None:
        mobjects = [animation.mobject] + scene.mobjects
    else:
        mobjects = scene.mobjects
    for scene_mobject in mobjects:
        # Check if the Mobjet has already been serialized.
        scene_mobject_id = id(scene_mobject)
        mobject_already_serialized = False
        for mobject_id in mobject_serializations:
            if scene_mobject_id == mobject_id:
                mobject_already_serialized = True
                break
        if not mobject_already_serialized:
            # This is a new Mobject; serialize it.
            mobject_serializations[scene_mobject_id] = serialize_mobject(scene_mobject)
    return mobject_serializations

def update_current_mobject_serializations(scene_seriaization, mobject_serializations):
    for mobject_serialization in scene_seriaization:
        mobject_id = mobject_serialization["id"]
        mobject_serializations[mobject_id] = mobject_serialization
    return mobject_serializations

def pointwise_function_wrapper(func):
    def wrapper(js_point):
        return func(pyodide.as_nested_list(js_point))
    return wrapper

def animation_to_json(play_args, play_kwargs):
    animation = play_args[0]
    if animation.__class__.__name__ == "ApplyPointwiseFunction":
        args = animation.get_args()
        return {
          "className": animation.__class__.__name__,
          "args": animation.args,
          "config": animation.config,
          "durationSeconds": animation.run_time,
          "func": pointwise_function_wrapper(args[0]),
        }
    else:
        return {
          "className": animation.__class__.__name__,
          "args": animation.args,
          "config": animation.config,
          "durationSeconds": animation.run_time,
        }

def wait_to_json(duration, stop_condition):
    return {
        "className": "Wait",
        "args": [],
        "durationSeconds": duration,
        "stopCondition": stop_condition,
        "description": "Hold a still frame",
        "argDescriptions": [],
    }

def scene_mobjects_to_json(mobjects):
    return list(map(lambda mob: {
        "name": id(mob),
        "submobjects": scene_mobjects_to_json(mob.submobjects),
    }, mobjects))

def mobject_to_json(mob):
    from manimlib.mobject.mobject import Group, Mobject
    from manimlib.mobject.types.vectorized_mobject import VMobject, VGroup
    if isinstance(mob, VMobject):
        ret = {
            "className": mob.__class__.__name__,
            "params": mob.kwargs,
            "position": mob.get_center(),
            "style": get_mobject_style(mob),
            "submobjects": [id(mob) for mob in mob.submobjects],
            "transformations": mob.transformations,
        }
        return ret
    elif type(mob) in [Group, Mobject, VGroup, VMobject]:
        return {
            "className": mob.__class__.__name__,
            "params": mob.kwargs,
            "submobjects": [id(mob) for mob in mob.submobjects],
            "transformations": mob.transformations,
        }
    else:
        print(mob)
        raise NotImplementedError("Mobject not available in javascript")


def get_mobject_style(mob):
    return {
        "strokeColor": mob.get_stroke_color().get_hex(),
        "strokeOpacity": mob.get_stroke_opacity(),
        "fillColor": mob.get_fill_color().get_hex(),
        "fillOpacity": mob.get_fill_opacity(),
        "strokeWidth": mob.get_stroke_width(),
    }

def tex_to_points(tex):
    if sys.platform == "emscripten":
        return pyodide.as_nested_list(js.texToPoints(tex))
    else:
        print("searching cache for " + tex)
        return tex2points(tex)
