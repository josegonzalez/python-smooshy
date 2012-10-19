=======
smooshy
=======


Huh?
====

This is a simple script written in Python to compress images. Often, images aren't as small as they could be.

Smooshy.py solves this problem by allowing you to compress all of those nasty extra bytes away without all the usual confusion surrounding fiddling around in the Save for Web Photoshop dialog.

How?
====

In fact, Smooshy is basically just a script which takes advantage of the awesome [smush.it](http://smush.it/) -- all your images are sent for compression over to smush.it -- so [be careful you don't send something you want to keep ultra-private](http://smush.it/faq.php).

It's all safe
=============

Smooshy creates backups of all your files while it's sprinkling its pixie dust over your images. If something goes wrong, your originals won't disappear into a black hole.

Also, if the resulting smooshed file is no smaller than the original, it won't be used.

Requirements
============

* simplejson - http://pypi.python.org/pypi/simplejson/
* Python 2.5 - http://www.python.org/download/releases/2.5/ or above (probably not Python 3, though)


Usage
=====

Current Directory::

		cd <directory of your choice>
		smooshy .

Specific files/directories::

		smooshy <as many files or directories as you'd like to smush here>


Within Python::

    from smooshy import smoosher
    smoosher.Smoosher(<file path).smoosh()
    # Smooshes the file
    smoosher.recursive_smoosher([<file or directory>... ])
    # Smooshes all files / all files recursively in directories

Installation
============

Using PIP:

From Github::

    pip install git+git://github.com/josegonzalez/smooshy.git#egg=smooshy

From PyPI::

    pip install smooshy==1


Credits
=======

Lots of people
