"""Create the panel/UI for interacting with the tool."""

import bpy


class VertexGroupEditorPanel(bpy.types.Panel):
    """The UI panel for interacting with the add on"""
    bl_label = "Vertex Group Editor"
    bl_idname = "VERTEXGROUP_PT_MAINPANEL"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        # Add/Delete section header.
        row = layout.row()
        row.label(text="Add or Delete Suffix")
        # Field to enter suffix.
        row = layout.row()
        row.prop(context.scene.vertex_group_editor, "suffix")
        # Add suffix button.
        row = layout.row()
        row.operator('object.add_suffix')
        # Delete suffix button.
        row = layout.row()
        row.operator('object.delete_suffix')
        # Delete groups with suffix button.
        row = layout.row()
        row.operator('object.delete_groups_with_suffix')
        # Delete groups without suffix button.
        row = layout.row()
        row.operator('object.delete_groups_without_suffix')
        # Delete groups except section header.
        row = layout.row()
        row.label(text="Delete all groups except:")
        # Field for entering group names to save.
        row = layout.row()
        row.prop(context.scene.vertex_group_editor, "groups")
        # Delete groups except button.
        row = layout.row()
        row.operator('object.delete_groups_except')


def register():
    """Register the VertexGroupEditorPanel class."""
    bpy.utils.register_class(VertexGroupEditorPanel)


def unregister():
    """Unregister the VertexGroupEditorPanel class."""
    bpy.utils.unregister_class(VertexGroupEditorPanel)