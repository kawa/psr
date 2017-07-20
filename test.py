import os
import time
from subprocess import Popen

def start_process(stdout):
    # no need for `global logger` you don't assign to it
    command = ['omxplayer --refresh ps.mp4']
    logger.debug(command) # no need for if(debug); set logging level instead
    return Popen(command, stdout=stdout) # run directly

# no need to use threads; Popen is asynchronous
with open('/tmp/scripts_output.txt') as file:
    process = start_process(file)
    time.sleep(4)
    p.terminate()
