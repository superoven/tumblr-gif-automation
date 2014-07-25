from receive import get_time
from process import output, tag
from bot import upload_gif
from config import FIFO


def main():
    while 1:
        with open(FIFO, "r") as f:
            fail_status, output_filename = output(get_time(f), get_time(f), f)
            if not fail_status:
                upload_gif(output_filename, tag(output_filename))

main()