import bpy

class DeleteGroupsWith(bpy.types.Operator):
    """Delete vertex groups that end with suffix"""
    bl_label = "Delete Groups With"
    bl_idname = "object.delete_groups_with_suffix"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        suffix = context.scene.vertex_group_editor.suffix
        object = bpy.context.view_layer.objects.active
        self.remove_vertex_groups_with_suffix(object, suffix)     
        return {'FINISHED'}
    
    def remove_vertex_groups_with_suffix(self, object, suffix):
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            removed = 0
            for group in object.vertex_groups:
                if group.name.endswith(suffix):
                    object.vertex_groups.remove(group)
                    removed += 1
            removed = str(removed)
            print("removed " + removed + " vertex groups with suffix " + suffix)

def register():
    bpy.utils.register_class(DeleteGroupsWith)

def unregister():
    bpy.utils.unregister_class(DeleteGroupsWith)