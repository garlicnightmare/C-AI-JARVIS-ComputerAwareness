import bpy
import sys

addon_dir = sys.argv[-1]
sys.path.insert(0, addon_dir)

bpy.ops.preferences.addon_enable(module="jarvis_scene_bridge")
bpy.ops.wm.save_userpref()

print("JARVIS Scene Bridge enabled and preferences saved.")
