import os
import time
import signal
import subprocess
from subprocess import Popen

FNULL = open(os.devnull, 'w')
process = Popen(["/opt/retropie/emulators/retroarch/bin/retroarch", "-L", "/opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so", "/home/pi/RetroPie/roms/psx/kurassyu_01.iso"], stdout=FNULL, stderr=subprocess.STDOUT)
time.sleep(4)
process.send_signal(signal.SIGINT)
process.wait()
