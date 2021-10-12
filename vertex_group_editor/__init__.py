"""Register all the modules in this package with Blender.

This module's approach adapted from: 
https://b3d.interplanety.org/en/creating-multifile-add-on-for-blender/
"""

import sys
import importlib

# Add-On Description For Blender
bl_info = {
    "name": "Vertex Group Editor",
    "description": "Easily edit Vertex Group names.",
    "author": "Ingrate, LLC",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object",
}

# Modules in this package. Each needs to be registered with Blender; each has
# its own registration logic.
modulesNames = [
    'add_suffix',
    'delete_groups_except',
    'delete_groups_with',
    'delete_groups_without',
    'delete_suffix',
    'vertex_group_editor_panel',
    'vertex_group_editor_settings',
]

# Load or reload all modules with the system. This logic runs/reruns whenever
# the user chooses to reload scripts.
modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(
        __name__, currentModuleName))
for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(
            currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames',
                modulesFullNames)


def register():
    """Register each module with Blender."""
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()


def unregister():
    """Unregister each module with Blender."""
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()


if __name__ == "__main__":
    register()
