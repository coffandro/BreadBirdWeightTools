_needs_reload = "bpy" in locals()

import bpy
from . import main

if _needs_reload:
    import importlib
    main = importlib.reload(main)
    print("BBG Weight Paints Add-on Reloaded")

def register():
    bpy.utils.register_class(main.HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(main.HelloWorldPanel)


if __name__ == "__main__":
    register()