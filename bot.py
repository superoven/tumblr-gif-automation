import requests
import json
from urlparse import parse_qs
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
import pytumblr
import simplejson

keyfile = "/home/taylor/.tumblr_keys"

f = open(keyfile, "r")
client_key = f.readline().rstrip()
client_secret = f.readline().rstrip()
resource_owner_key = f.readline().rstrip()
resource_owner_secret = f.readline().rstrip()
f.close()

print client_key
print client_secret
print resource_owner_key
print resource_owner_secret

"""client = pytumblr.TumblrRestClient(
    client_key,
    client_secret,
    resource_owner_key,
    resource_owner_secret
)

derp = client.create_photo('superoven', state="publish", tags=["yolo", "swag"], format="markdown", data=["image.jpg", "image2.jpg"], caption="autopost")

print simplejson.dumps(derp, indent=2)
"""
