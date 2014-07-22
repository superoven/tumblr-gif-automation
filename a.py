import datetime
from subprocess import call
from os import listdir,devnull
from os.path import isfile, join
import filecmp
import uuid
import sys

FNULL = open(devnull)

fifo = '/home/taylor/.mplayer_fifo.out'
baseDirectory = '/tmp/mplayer'
outputDirectory = 'output'

def getFileName(f):
    call(["./sendm", "get_file_name"])
    return waitForString(f, 'ANS_FILENAME')

def getTime(f):
    return waitForFloat(f, 'ANS_TIME_POSITION')

def waitForFloat(f, name):
    return float(waitForString(f, name))

def waitForInt(f, name):
    return int(waitForString(f, name))

def sanitize(s):
    return s.rstrip().rstrip("'").lstrip().lstrip("'")

def waitForString(f, name):
    while 1:
        try:
            val = f.readline().split('=')
            if len(val) == 2 and val[0] == name:
                return sanitize(val[1])
        except:
            quit()

def tag(outputDirectory, uid, filename):
    #TODO: Infer basic tags, get translations of names
    results = raw_input("Type comma separated tags: ")
    print results.split(",")
    with open("%s/%s.tag" % (outputDirectory, uid), "w") as f:
        print >> f, results

def yesNo(question):
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    while 1:
        choice = raw_input(question).lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        print "Please respond with 'yes' or 'no'"

def output(first, last, f):
    uid = str(uuid.uuid4())
    out = "%s/%s.gif" % (outputDirectory, uid)
    directory = "%s/%s" % (baseDirectory, uid)
    call(["mkdir", baseDirectory], stdout=FNULL, stderr=FNULL)
    call(["mkdir", directory], stdout=FNULL, stderr=FNULL)
    filename = getFileName(f)
    print "FILENAME:",filename
    command = ["./ripimages", str(first), str(last - first),
               filename, directory]
    call(command)
    print "Output to:", directory
    command = ["./makegif", str(len(listdir(directory))), out, directory]
    print "Making GIF(s)..."
    call(command)
    print "GIF Created:", out
    call(["eog", out])
    if yesNo("Want to save and tag this image for upload? [y/n]: "):
        print "Saved."
        tag(outputDirectory, uid, filename)
    else:
        call(["rm", "-f", out])
        print "Yeah, I didn't like that one either."
    
    
while 1:
    with open(fifo, "r") as f:
        print "--- Ready to make a GIF ---"
        output(getTime(f), getTime(f), f)
