 #!/usr/bin/env python

import subprocess
import sys
import time

#ABS_PATH_WAV2RAW = '/home/carlos/TFG_Carlos/wav2raw'
#ABS_PATH_RAW2CC = '/home/carlos/TFG_Carlos/raw2CC'


def run(ABS_PATH):
    res = subprocess.call(ABS_PATH)
    if res == 0:
        return "success"
    else:
        return "failure"

    #process = Popen([ABS_PATH_IATROS_RUN], stdout=PIPE, stderr=PIPE)
    #stdout, stderr = process.communicate()
    #print stdout

if __name__ == "__main__":
    run(sys.argv[1])
