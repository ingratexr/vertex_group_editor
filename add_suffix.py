import bpy

class AddSuffix(bpy.types.Operator):
    """Add suffix to all the object's vertex groups that don't end with it already"""
    bl_label = "Add To Groups"
    bl_idname = "object.add_suffix"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        suffix = context.scene.vertex_group_editor.suffix
        object = bpy.context.view_layer.objects.active
        self.append_vertex_group_names(object, suffix)        
        return {'FINISHED'}
    
    def append_vertex_group_names(self, object, suffix):        
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            for group in object.vertex_groups:
                group.name += suffix
                print(group.name)
            print("done")

def register():
    bpy.utils.register_class(AddSuffix)

def unregister():
    bpy.utils.unregister_class(AddSuffix)