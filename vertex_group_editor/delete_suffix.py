"""Delete the suffix from any vertex group name that ends with it."""

import bpy


class DeleteSuffix(bpy.types.Operator):
    """Delete suffix from any of the object's vertex groups that end with it"""
    bl_label = "Remove From Groups"
    bl_idname = "object.delete_suffix"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        """Execute function runs when operator is called."""
        suffix = context.scene.vertex_group_editor.suffix
        object = bpy.context.view_layer.objects.active
        self.remove_vertex_group_suffix(object, suffix)
        return {'FINISHED'}

    def remove_vertex_group_suffix(self, object, suffix):
        """Remove the suffix from any of the object's vertex group names that
        end with it.

        Args:
        object:
            The object whose vertex groups to manipulate.
        suffix:
            String to delete from the end of any vertex group names that end 
            with it.
        """
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            for group in object.vertex_groups:
                if group.name.endswith(suffix):
                    group.name = group.name[:-len(suffix)]
                print(group.name)


def register():
    """Register the DeleteSuffix class."""
    bpy.utils.register_class(DeleteSuffix)


def unregister():
    """Unregister the DeleteSuffix class."""
    bpy.utils.unregister_class(DeleteSuffix)