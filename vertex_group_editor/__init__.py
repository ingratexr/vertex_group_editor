'''
Copyright (C) 2021 Ingrate, LLC
info@ingratexr.com
Created by John Hudson.
'''

bl_info = {
    "name": "Vertex Group Editor",
    "description": "Easily edit Vertex Group names.",
    "author": "Ingrate, LLC",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }

# Modules in this package
# Might be important that vertex_group_editor_settings is listed before vertex_group_editor_panel
modulesNames = ['add_suffix', 
                'delete_groups_except', 
                'delete_groups_with',
                'delete_groups_without',
                'delete_suffix',
                'vertex_group_editor_settings',
                'vertex_group_editor_panel']

import sys
import importlib

# Build dictionary with full module names
modulesFullNames = {}
for currentModuleName in modulesNames:
    modulesFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

# Either reload or initially load all modules
for currentModuleFullName in modulesFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'modulesNames', modulesFullNames)

# Go through modules and run each one's register function, if it exists
# Each module has its own register function so that it can run more logic if it needs to
# (As opposed to listing each class here and then registering them in a for loop here)
def register():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

# Go through modules and run each one's unregister function, if it exists
def unregister():
    for currentModuleName in modulesFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()
 
if __name__ == "__main__":
    register()