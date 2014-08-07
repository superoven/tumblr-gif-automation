from receive import ReceiveEngine
import Tkinter as tk
import subprocess
import sys
import fcntl
import os


def main(filename):
    cmd = ['mplayer', '-slave', '-quiet', filename]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE)
    fcntl.fcntl(p.stdout.fileno(), fcntl.F_SETFL,
                fcntl.fcntl(p.stdout.fileno(), fcntl.F_GETFL) | os.O_NONBLOCK)

    root = tk.Tk()
    s = ReceiveEngine(p, root, filename)

    def onKeyPress(event):
        if event.char == 'q':
            s.kill()
        elif event.char == 'a':
            s.perform_command('get_time_pos', 'ANS_TIME_POSITION')
        else:
            pass

    root.bind('<KeyPress>', onKeyPress)
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        subprocess.call(["mplayer"])
        exit()
    main(sys.argv[1])
