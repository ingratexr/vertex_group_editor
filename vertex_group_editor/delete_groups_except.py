"""Delete all of the active object's vertex groups except those specified."""

import bpy


class DeleteGroupsExcept(bpy.types.Operator):
    """Delete all vertex groups except those listed"""
    bl_label = "Delete Groups Except"
    bl_idname = "object.delete_groups_except"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Execute function runs when operator is called."""
        groups = context.scene.vertex_group_editor.groups
        object = bpy.context.view_layer.objects.active
        self.delete_groups(object, groups.lower())
        return {'FINISHED'}

    def delete_groups(self, object, keepers):
        """Deletes all vertex groups whose names don't appear in arg keeps.

        Removes any vertex group name that is not a substring of the keepers 
        string, so it doesn't matter how the user delineates group names to keep
        (ie with whitespace, commas, both, neither). Not case sensitive.

        Args:
        object:
            The object whose vertex group names to change.
        keepers:
            String containing all vertex group names to keep.
        """
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            counter = 0
            for group in object.vertex_groups:
                if group.name.lower() not in keepers:
                    object.vertex_groups.remove(group)
                    counter += 1
            print('removed {} vertex groups'.format(str(counter)))


def register():
    """Register the DeleteGroupsExcept class."""
    bpy.utils.register_class(DeleteGroupsExcept)


def unregister():
    """Unregister the DeleteGroupsExcept class."""
    bpy.utils.unregister_class(DeleteGroupsExcept)