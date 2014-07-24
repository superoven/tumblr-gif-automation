import pytumblr
import simplejson

key_file = "/home/taylor/.tumblr_keys"
tags_file = "/home/taylor/.tumblr_default_tags"

with open(key_file, "r") as f:
    client_key = f.readline().rstrip()
    client_secret = f.readline().rstrip()
    resource_owner_key = f.readline().rstrip()
    resource_owner_secret = f.readline().rstrip()

with open(tags_file, 'r') as f:
    tags = f.read().split(',')


def upload_gif(filename, additional_tags):
    resp = pytumblr.TumblrRestClient(
        client_key,
        client_secret,
        resource_owner_key,
        resource_owner_secret
    ).create_photo('superoven', state="draft", tags=tags + additional_tags,
                               format="markdown", data=[filename])
    print simplejson.dumps(resp, indent=2)
