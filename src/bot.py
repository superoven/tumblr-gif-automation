import pytumblr
import simplejson
from config import KEY_FILE


with open(KEY_FILE, "r") as f:
    username = f.readline().rstrip()
    client_key = f.readline().rstrip()
    client_secret = f.readline().rstrip()
    resource_owner_key = f.readline().rstrip()
    resource_owner_secret = f.readline().rstrip()


def upload_gif(filename, tags):
    resp = pytumblr.TumblrRestClient(
        client_key,
        client_secret,
        resource_owner_key,
        resource_owner_secret
    ).create_photo(username, state="draft", tags=tags,
                   format="markdown", data=[filename])
    print simplejson.dumps(resp, indent=2)
