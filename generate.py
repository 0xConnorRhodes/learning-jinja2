#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)
