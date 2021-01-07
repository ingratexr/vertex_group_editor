import bpy

class DeleteGroupsExcept(bpy.types.Operator):
    """Delete vertex groups except those listed"""
    bl_label = "Delete Groups Except"
    bl_idname = "object.delete_groups_except"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        groups = context.scene.vertex_group_editor.groups
        object = bpy.context.view_layer.objects.active
        self.delete_groups(object, groups)
        return {'FINISHED'}
    
    def string_to_list(self, string):
        string = self.remove_commas(string)
        return list(string.split(" "))    
        
    def remove_commas(self, string):
        return string.replace(", ", " ")
    
    def delete_groups(self, object, keepers):
        if not object.vertex_groups:
            print("no vertex groups")
        else:
            counter = 0
            for group in object.vertex_groups:
                if group.name not in keepers:
                    object.vertex_groups.remove(group)
                    counter += 1
            print("removed " + str(counter) + " vertex groups")

def register():
    bpy.utils.register_class(DeleteGroupsExcept)

def unregister():
    bpy.utils.unregister_class(DeleteGroupsExcept)