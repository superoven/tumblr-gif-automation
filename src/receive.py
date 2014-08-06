from subprocess import call
from config import ROOT_DIR, INPUT_FIFO
from urlparse import urljoin

YES_ANSWERS = {'', 'y', 'ye', 'yes'}
NO_ANSWERS = {'n', 'no'}


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


def getfilename(file_desc):
    call([urljoin(ROOT_DIR, "scripts/sendm"), "get_file_name"])
    return wait_string(file_desc, 'ANS_FILENAME')


def get_time(file_desc):
    capture_input()
    return wait_float(file_desc, 'ANS_TIME_POSITION')


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
