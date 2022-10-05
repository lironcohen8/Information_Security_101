# The fetch(url) function fetches a page from the web. To avoid re-fetching the same pages twice, which is pretty slow,
# it caches them per user (it figures out the current user by looking at os.environ['USER']).
#
# Write a function, did_fetch(user, url), that figures out whether some user has fetched some url or not.
# You can assume fetching a resource from the web takes at least 0.1 seconds,
# while fetching it from the cache is near immediate.

import os
import time
import sys # ignore
sys.path.insert(0,'.') # ignore

_cache = {}
def fetch(url):
    user = os.environ['USER']
    if user not in _cache:
        _cache[user] = {}
    if url not in _cache[user]:
         _cache[user][url] = requests.get(url).content
    return _cache[user][url]


def did_fetch(user, url):
    os.environ['USER'] = user
    start_time = time.time()
    fetch(url)
    end_time = time.time()
    fetch_time = end_time - start_time
    return fetch_time <= 0.1