import os
import time
import signal
import subprocess
from subprocess import Popen

startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
process = Popen(["/opt/retropie/emulators/retroarch/bin/retroarch", "-L", "/opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so", "/home/pi/RetroPie/roms/psx/kurassyu_01.iso"], startupinfo=startupinfo)
time.sleep(4)
process.send_signal(signal.SIGINT)
process.wait()
