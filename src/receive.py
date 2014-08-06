from subprocess import call
from config import ROOT_DIR, INPUT_FIFO
from urlparse import urljoin
import select

YES_ANSWERS = {'', 'y', 'ye', 'yes'}
NO_ANSWERS = {'n', 'no'}


def send_command(p, cmd):
    p.stdin.write(cmd + '\n')


def send_time_request():
    with open(INPUT_FIFO, 'w') as f:
        print >>f, "get_time_pos"


def capture_input():
    val = raw_input("-- Press Enter to capture --")
    while val != '\n':
        val = raw_input()
        if val[0] == 'q':
            quit()
    send_time_request()


def getfilename(p):
    return wait_command(p, 'ANS_FILENAME')


def get_time(p):
    return send_command(p, "get_time_pos")


def wait_command(p, expect):
    while 1:
        out = p.stdout.readline()
        split_output = out.split(expect + '=', 1)
        if len(split_output) == 2 and split_output[0] == '':
            value = split_output[1]
            return float(value.rstrip())


def wait_float(file_desc, name):
    return float(wait_string(file_desc, name))


def wait_int(file_desc, name):
    return int(wait_string(file_desc, name))


def sanitize(s):
    return s.rstrip().rstrip("'").lstrip().lstrip("'")


def wait_string(file_desc, name):
    while 1:
        try:
            val = file_desc.readline().split('=')
            if len(val) == 2 and val[0] == name:
                return sanitize(val[1])
        except IOError:
            quit()


def yes_or_no(question):
    while 1:
        choice = raw_input(question).lower()
        if choice in YES_ANSWERS:
            return True
        elif choice in NO_ANSWERS:
            return False
        print "Please respond with 'yes' or 'no'"
