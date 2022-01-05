#!/usr/bin/python
# Made using this tutorial: https://medium.com/@jasonrigden/jinja2-templating-engine-tutorial-4bd31fb4aea3

#import jinja2
from jinja2 import Environment, FileSystemLoader

# pass the directory containing the templates to FileSystemLoader
file_loader = FileSystemLoader('templates')

# load the environment
env = Environment(loader=file_loader)

# load the template
template = env.get_template('hello_world.txt')

# render and pring
output = template.render()
print(output)
