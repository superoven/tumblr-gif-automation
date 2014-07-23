from receive import get_time
from process import output, fifo

while 1:
    with open(fifo, "r") as f:
        output(get_time(f), get_time(f), f)
