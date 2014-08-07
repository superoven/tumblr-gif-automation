from process import output, tag


class ReceiveEngine:
    def __init__(self, p, root, filename):
        self.vals = []
        self.filename = filename
        self.root = root
        self.p = p

    def perform_command(self, cmd, expect):
        import select
        self.p.stdin.write(cmd + '\n')
        while select.select([self.p.stdout], [], [], 0.05)[0]:
            out = self.p.stdout.readline()
            split_output = out.split(expect + '=', 1)
            if len(split_output) == 2 and split_output[0] == '':
                value = split_output[1]
                self.vals.append(float(value.rstrip()))
                if len(self.vals) >= 2:
                    first = self.vals[0]
                    second = self.vals[1]
                    self.vals = []
                    fail_status, output_filename = output(first, second, self.filename)
                    if not fail_status:
                        tag(self.filename, output_filename)
                    return

    def kill(self):
        self.root.quit()
        self.p.kill()

YES_ANSWERS = {'', 'y', 'ye', 'yes'}
NO_ANSWERS = {'n', 'no'}


def yes_or_no(question):
    while 1:
        choice = raw_input(question).lower()
        if choice in YES_ANSWERS:
            return True
        elif choice in NO_ANSWERS:
            return False
        print "Please respond with 'yes' or 'no'"
