#!/usr/bin/python3.6

"""MetaCall Examples - Python Time App Web.

[MetaCall](https://metacall.io)
[MetaCall Examples](https://github.com/metacall/examples)

This modules demonstrates a basic example of a python backend that serves
an html index and returns the current hour in just two functions.

""" 

from os import path
from datetime import datetime


def index():
  """Read index.html from file and return it.

  Returns:
    Return the index.html content.
  """
  basepath = path.dirname(path.abspath(__file__))

  with open(path.join(basepath, 'index.html'), 'r') as f:
    return f.read()

def time():
  """Get current time and date.

  Returns:
    Current time and date as a formatted string.
  """
  return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
