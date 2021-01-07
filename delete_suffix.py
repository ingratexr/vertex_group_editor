import bpy

class DeleteSuffix(bpy.types.Operator):
    """Delete suffix from any of the object's vertex groups that end with it"""
    bl_label = "Remove From Groups"
    bl_idname = "object.delete_suffix"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        suffix = context.scene.vertex_group_editor.suffix
        object = bpy.context.view_layer.objects.active
        self.remove_vertex_group_suffix(object, suffix)       
        return {'FINISHED'}
    
    def remove_vertex_group_suffix(self, object, suffix):
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            for group in object.vertex_groups:
                if group.name.endswith(suffix):
                    group.name = group.name[:-len(suffix)]
                print(group.name)

def register():
    bpy.utils.register_class(DeleteSuffix)

def unregister():
    bpy.utils.unregister_class(DeleteSuffix)