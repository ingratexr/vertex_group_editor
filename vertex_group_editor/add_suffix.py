"""Adds specified suffix to all of the active object's vertex groups"""

import bpy


class AddSuffix(bpy.types.Operator):
    """Appends suffix to the names of all the active object's vertex groups.
    """
    bl_label = "Add To Groups"
    bl_idname = "object.add_suffix"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Execute function runs when operator is called."""
        suffix = context.scene.vertex_group_editor.suffix
        object = bpy.context.view_layer.objects.active
        self.append_vertex_group_names(object, suffix)
        return {'FINISHED'}

    def append_vertex_group_names(self, object, suffix):
        """Appends suffix to each of the object's vertex groups' names.

        Args:
        object:
            The object whose vertex groups are going to be manipulated.
        suffix:
            The suffix to append.
        """
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            for group in object.vertex_groups:
                group.name += suffix
                print(group.name)
            print("done")


def register():
    """Register the AddSuffix class."""
    bpy.utils.register_class(AddSuffix)


def unregister():
    """Unregister the AddSuffix class."""
    bpy.utils.unregister_class(AddSuffix)