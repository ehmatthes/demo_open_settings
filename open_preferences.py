"""Open the operating system's System Preferences,
or equivalent."""

import subprocess, shlex

cmd = "open '/System/Applications/System Settings.app'"
cmd_parts = shlex.split(cmd)
subprocess.run(cmd_parts)