from subprocess import call
from receive import getfilename, yes_or_no
from shell_calls import make_temp_dir, rip_images, make_gif, open_gif
import uuid


fifo = '/home/taylor/.mplayer_fifo.out'
baseDirectory = '/tmp/mplayer'
outputDirectory = 'output'


def tag(output_directory, uid, filename, output_filename):
    #TODO: Infer basic tags, get translations of names
    if not yes_or_no("Want to save and tag this image for upload? [y/n]: "):
        call(["rm", "-f", output_filename])
        print "Yeah, I didn't like that one either."
        return
    results = raw_input("Type comma separated tags: ")
    with open("%s/%s.tag" % (output_directory, uid), "w") as f:
        print >> f, results


def output(first, second, file_desc):
    uid = str(uuid.uuid4())
    output_filename = "%s/%s.gif" % (outputDirectory, uid)
    temp_directory = make_temp_dir(baseDirectory, uid)
    filename = getfilename(file_desc)
    rip_images(first, second, filename, temp_directory) \
      or make_gif(temp_directory, output_filename) \
      or open_gif(output_filename)
    tag(outputDirectory, uid, filename, output_filename)
