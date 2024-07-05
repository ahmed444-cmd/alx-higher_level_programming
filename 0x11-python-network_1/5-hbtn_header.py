#!/usr/bin/python3
"""A script that
takes a URL as input
sends an HTTP request to the given URL
displays the X-Request-Id header from the response """
from requests import get
from sys import argv


def get_alx_intranet(url):

    if url:
        try:
            return get(url).headers.get('X-Request-Id')
        except Exception as e:
            return e


if __name__ == "__main__":
    print(get_alx_intranet(argv[1]))
