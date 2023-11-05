"""Open the operating system's System Preferences,
or equivalent."""

import os, platform, subprocess, shlex

if platform.system() == "Darwin":
    cmd = "open '/System/Applications/System Settings.app'"
    cmd_parts = shlex.split(cmd)
    subprocess.run(cmd_parts)
elif platform.system() == 'Windows':
    cmd = os.system("control")
