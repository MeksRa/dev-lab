# package => is just a collection of modules in a directory.
# it also contains __init__.py file to indicate that it's a package.
# __init__ file can either be empty or it can define some initialization code for a package.
from my_package import internet, website

internet.connect()
website.load("www.google.com")


# Difference between library and package

# module - book
# package - section
# library - library

# Library is a folder with packages and modules
# Package is a folder with modules
