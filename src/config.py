from os.path import join, normpath, abspath
from urlparse import urljoin

ROOT_DIR = normpath(join(abspath(__file__), '..'))

BASE_DIRECTORY = '/tmp/mplayer'
OUTPUT_DIRECTORY = urljoin(ROOT_DIR, 'output')
TAGS_FILE = urljoin(ROOT_DIR, ".tumblr_default_tags")
KEY_FILE = "/home/taylor/.tumblr_keys"