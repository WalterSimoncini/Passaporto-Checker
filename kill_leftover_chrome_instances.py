# This program kills instances of Chrome that may have been left over
# by crashes of the main script

import os
import signal
import subprocess

def kill_chrome_instances():
    p = subprocess.Popen(['ps', '-A'], stdout = subprocess.PIPE)
    out, err = p.communicate()

    if err == None:
        for line in out.splitlines():
            if "chrome" in line or "chromedriver" in line:
                pid = pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)

kill_chrome_instances()