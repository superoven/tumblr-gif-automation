from receive import get_time
from process import output, tag
from bot import upload_gif
from config import FIFO
import subprocess
import sys


def main(filename):
    cmd = ['mplayer', '-slave', '-quiet', filename]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    while 1:
        # with open(FIFO, "r") as f:
        fail_status, output_filename = output(get_time(p), get_time(p), filename)
        if not fail_status:
            upload_gif(output_filename, tag(output_filename))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Give me a video file"
    main(sys.argv[1])