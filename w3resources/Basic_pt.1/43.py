#Write a Python program to get OS name, platform and release information.

#02_13_21

import os
import platform

print(f"Operating System: {os.name}")
print(f"Platform: {platform.system()}")
print(f"Release info: {platform.release()}")