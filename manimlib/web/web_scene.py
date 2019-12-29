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
    update_mobject_serializations,
)
from manimlib.mobject.mobject import Mobject, Group
from manimlib.mobject.svg.tex_mobject import (
    TexMobject,
    TextMobject,
    SingleStringTexMobject,
)


class WebScene(Scene):
    def __init__(self, **kwargs):
        self.scene_diffs = []
        self.animation_diffs = []
        self.initial_mobject_serializations = {}
        self.last_scene = []

        # A list of snapshots of the Scene before each Animation
        self.scenes_before_animation = []
        # A list of serialized Animations
        self.animation_list = []
        self.render_kwargs = kwargs
        # A mapping of IDs to Mobjects
        self.initial_mobject_dict = {}

    def render(self):
        # Regular Scenes render upon instantiation.
        return super(WebScene, self).__init__(**self.render_kwargs)

    def play(self, *args, **kwargs):
        # Compute scene diff
        self.initial_mobject_serializations = update_mobject_serializations(self, self.initial_mobject_serializations)
        cur_scene = serialize_scene(self)
        self.scene_diffs.append(scene_diff(self.last_scene, cur_scene))
        self.last_scene = cur_scene


        animation = args[0]
        if animation.__class__.__name__.startswith("ApplyPointwiseFunction"):
            self.update_initial_mobject_dict(mobject_list=[animation.mobject])
        else:
            self.update_initial_mobject_dict(mobject_list=animation.get_args())
        self.scenes_before_animation.append(scene_mobjects_to_json(self.mobjects))
        self.animation_list.append(animation_to_json(args, kwargs))
        super(WebScene, self).play(*args, **kwargs)


        # Compute animation diff
        self.initial_mobject_serializations = update_mobject_serializations(self, self.initial_mobject_serializations)
        cur_scene = serialize_scene(self)
        # TODO: Include any mobjects that are going to be animated but haven't been added to the scene.
        self.animation_diffs.append(scene_diff(self.last_scene, cur_scene, animation=animation))
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

    def tear_down(self):
        # convert scenes_before_animation to diffs?
        pass
