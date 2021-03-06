from subprocess import call
from os import devnull, listdir
from config import ROOT_DIR
from urlparse import urljoin


def make_temp_dir(base_dir, uid):
    with open(devnull) as dev_null:
        directory = "%s/%s" % (base_dir, uid)
        call(["mkdir", base_dir], stdout=dev_null, stderr=dev_null)
        call(["mkdir", directory], stdout=dev_null, stderr=dev_null)
        return directory


def rip_images(first_time, second_time, filename, temp_dir):
    first = str(first_time)
    delta = str(second_time - first_time)
    return call(["ffmpeg", "-ss", first,
                 "-i", filename,
                 "-t", delta,
                 "-s", "480x270",
                 "-f", "image2",
                 temp_dir + "/%03d.png"])


def make_gif(temp_directory, output_directory):
    print "Making GIF(s)..."
    return call([urljoin(ROOT_DIR, "scripts/makegif"), str(len(listdir(temp_directory))), output_directory, temp_directory])


def open_gif(filename):
    return call(["eog", filename])