import os
import time
from subprocess import Popen

process = Popen(["/opt/retropie/emulators/retroarch/bin/retroarch", "-L", "/opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so", "/home/pi/RetroPie/roms/psx/kurassyu_01.iso"])
time.sleep(4)
process.terminate()
