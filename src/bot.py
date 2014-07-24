import pytumblr
import simplejson

key_file = "/home/taylor/.tumblr_keys"

with open(key_file, "r") as f:
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
    ).create_photo('superoven', state="draft", tags=tags,
                   format="markdown", data=[filename])
    print simplejson.dumps(resp, indent=2)
