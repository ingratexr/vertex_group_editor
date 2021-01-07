import bpy

class DeleteGroupsWithout(bpy.types.Operator):
    """Delete vertex groups that do not end with suffix"""
    bl_label = "Delete Groups Without"
    bl_idname = "object.delete_groups_without_suffix"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        suffix = context.scene.vertex_group_editor.suffix
        object = bpy.context.view_layer.objects.active
        self.remove_vertex_groups_without_suffix(object, suffix)     
        return {'FINISHED'}
    
    def remove_vertex_groups_without_suffix(self, object, suffix):
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            removed = 0
            for group in object.vertex_groups:
                if not group.name.endswith(suffix):
                    object.vertex_groups.remove(group)
                    removed += 1
            removed = str(removed)
            print("removed " + removed + " vertex groups without suffix " + suffix)

def register():
    bpy.utils.register_class(DeleteGroupsWithout)

def unregister():
    bpy.utils.unregister_class(DeleteGroupsWithout)