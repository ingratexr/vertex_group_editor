import bpy

class VertexGroupEditorSettings(bpy.types.PropertyGroup):
    suffix: bpy.props.StringProperty(name = "Suffix",
                                    description = "Suffix to add to/remove from vertex groups",
                                    default = ".001",
                                    maxlen = 64)
    groups: bpy.props.StringProperty(name = "Groups",
                                    description = "Remove all vertex groups except these.\nSeparate groups with a space",
                                    default = "",
                                    maxlen = 1024)

def register():
    bpy.utils.register_class(VertexGroupEditorSettings)
    try:
        bpy.types.Scene.vertex_group_editor = bpy.props.PointerProperty(type=VertexGroupEditorSettings)
    except:
        print("there was an error registering vertex group editor settings")

def unregister():
    bpy.utils.unregister_class(VertexGroupEditorSettings)
    try:
        del bpy.types.Scene.vertex_group_editor
    except:
        print("there was an error unregistering vertex group editor settings")