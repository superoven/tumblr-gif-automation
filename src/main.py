from receive import get_time
from process import output, tag
from config import FIFO
import sys

while 1:
    with open(FIFO, "r") as f:
        print "--- Ready to make a GIF ---"
        fail_status, output_filename = output(get_time(f), get_time(f), sys.argv[1])
        if not fail_status:
            tags = tag(output_filename)

