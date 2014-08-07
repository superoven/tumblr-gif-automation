from subprocess import call
from receive import yes_or_no
from shell_calls import make_temp_dir, rip_images, make_gif, open_gif
from config import TAGS_FILE, OUTPUT_DIRECTORY, BASE_DIRECTORY
import uuid
from bot import upload_gif
import json


def get_title(filename):
    import re
    m = re.search('^.*\[.+\](.+) \- [0-9]+.*$', filename)
    return m.group(1).lstrip().rstrip()


def clean_tags(s):
    return map(lambda x: x.lstrip().rstrip(),s.split(','))


def get_tags(title):
    with open(TAGS_FILE, 'r+') as f:
        tags = json.loads(f.read().decode('UTF8'))
        if title in tags:
            return tags[title] + tags['default']
        else:
            print "The show: \"%s\" needs default tags." % title
            tags[title] = clean_tags(raw_input("Enter comma separated tags:"))
            f.seek(0)
            f.write(json.dumps(tags, ensure_ascii=False, encoding='utf8').encode("UTF8"))
            f.truncate()
            return tags[title] + tags['default']


def tag(filename, output_filename):
    if not yes_or_no("Want to save and tag this image for upload? [y/n]: "):
        call(["rm", "-f", output_filename])
        print "Yeah, I didn't like that one either."
        return
    additional_tags = raw_input("Type comma separated tags: ")
    upload_gif(output_filename, clean_tags(additional_tags) + get_tags(get_title(filename)))


def output(first, second, filename):
    uid = str(uuid.uuid4())
    output_filename = "%s/%s.gif" % (OUTPUT_DIRECTORY, uid)
    temp_directory = make_temp_dir(BASE_DIRECTORY, uid)
    ret_num = rip_images(first, second, filename, temp_directory) \
      or make_gif(temp_directory, output_filename) \
      or open_gif(output_filename)
    if ret_num:
        print "--- BREAKING GIF PIPELINE - GIF NOT CREATED ---"
    return ret_num, output_filename
