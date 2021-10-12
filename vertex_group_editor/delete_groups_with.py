"""Delete all the active object's vertex groups that end with the specified 
suffix."""

import bpy


class DeleteGroupsWith(bpy.types.Operator):
    """Delete all vertex groups that end with suffix"""
    bl_label = "Delete Groups With"
    bl_idname = "object.delete_groups_with_suffix"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Execute function runs when operator is called."""
        suffix = context.scene.vertex_group_editor.suffix
        object = bpy.context.view_layer.objects.active
        self.remove_vertex_groups_with_suffix(object, suffix)
        return {'FINISHED'}

    def remove_vertex_groups_with_suffix(self, object, suffix):
        """Deletes all object's vertex groups that don't end in suffix.

        Args:
        object:
            The object whose vertex groups to manipulate.
        suffix:
            Any of the object's vertex groups that end with this string will be
            deleted.
        """
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            removed = 0
            for group in object.vertex_groups:
                if group.name.endswith(suffix):
                    object.vertex_groups.remove(group)
                    removed += 1
            removed = str(removed)
            print('removed {} vertex groups with the suffix {}'.format(
                removed, suffix))


def register():
    """Register the DeleteGroupsWith class."""
    bpy.utils.register_class(DeleteGroupsWith)


def unregister():
    """Unregister the DeleteGroupsWith class."""
    bpy.utils.unregister_class(DeleteGroupsWith)