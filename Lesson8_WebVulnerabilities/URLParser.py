# Implement a function that given a URL, parses it and returns a tuple with its protocol, domain and path.
# For example, for "http://www.google.com/search", it whould return ('http', 'www.google.com', '/search').

from urllib.parse import urlparse


def parse_url(url):
    parsed_url = urlparse(url)
    protocol = parsed_url.scheme
    domain = parsed_url.netloc
    path = parsed_url.path
    return protocol, domain, path