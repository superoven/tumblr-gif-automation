from subprocess import call

YES_ANSWERS = {'', 'y', 'ye', 'yes'}
NO_ANSWERS = {'n', 'no'}


def getfilename(file_desc):
    call(["scripts/sendm", "get_file_name"])
    return wait_string(file_desc, 'ANS_FILENAME')


def get_time(file_desc):
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
