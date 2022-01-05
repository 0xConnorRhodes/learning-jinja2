#!/usr/bin/python
from jinja2 import Environment, FileSystemLoader

file_loader = FileSystemLoader('templates')

env = Environment(loader=file_loader)

template = env.get_template('hello_world.txt')

output = template.render()
print(output)
