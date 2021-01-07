import bpy

__reload_order_index__: 6

class VertexGroupEditorPanel(bpy.types.Panel):
    bl_label = "Vertex Group Editor"
    bl_idname = "VERTEXGROUP_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Add or Delete Suffix")
        row = layout.row()
        row.prop(context.scene.vertex_group_editor, "suffix")
        row = layout.row()
        row.operator('object.add_suffix')
        row = layout.row()
        row.operator('object.delete_suffix')
        row = layout.row()
        row.operator('object.delete_groups_with_suffix')
        row = layout.row()
        row.operator('object.delete_groups_without_suffix')
        row = layout.row()
        row.label(text = "Remove all groups except:")
        row = layout.row()
        row.prop(context.scene.vertex_group_editor, "groups")
        row = layout.row()
        row.operator('object.delete_groups_except')

def register():
    bpy.utils.register_class(VertexGroupEditorPanel)

def unregister():
    bpy.utils.unregister_class(VertexGroupEditorPanel)