from subprocess import call
from receive import getfilename, yes_or_no
from shell_calls import make_temp_dir, rip_images, make_gif, open_gif
from config import TAGS_FILE, OUTPUT_DIRECTORY, BASE_DIRECTORY
import uuid


def clean_tags(s):
    return s.split(',').map(lambda x: x.lstrip().rstrip())

with open(TAGS_FILE, 'r') as f:
    default_tags = clean_tags(f.read())


def tag(output_filename):
    #TODO: Infer basic tags, get translations of names
    if not yes_or_no("Want to save and tag this image for upload? [y/n]: "):
        call(["rm", "-f", output_filename])
        print "Yeah, I didn't like that one either."
        return
    additional_tags = raw_input("Type comma separated tags: ")
    return default_tags + clean_tags(additional_tags)


def output(first, second, file_desc):
    uid = str(uuid.uuid4())
    output_filename = "%s/%s.gif" % (OUTPUT_DIRECTORY, uid)
    temp_directory = make_temp_dir(BASE_DIRECTORY, uid)
    filename = getfilename(file_desc)
    ret_num = rip_images(first, second, filename, temp_directory) \
      or make_gif(temp_directory, output_filename) \
      or open_gif(output_filename)
    return ret_num, output_filename
