import os
import time
from subprocess import Popen

def start_process(stdout):
    # no need for `global logger` you don't assign to it
    command = ["/opt/retropie/emulators/retroarch/bin/retroarch -L /opt/retropie/libretrocores/lr-pcsx-rearmed/libretro.so ~/RetroPie/roms/psx/kurassyu_01.iso"]
    return Popen(command, stdout=stdout) # run directly

# no need to use threads; Popen is asynchronous
with open('/tmp/scripts_output.txt') as file:
    process = start_process(file)
    time.sleep(4)
    p.terminate()