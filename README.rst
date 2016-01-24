irename
=======

``irename`` allows to easy rename many files using Your favorite editor.

When You call ``irename`` (with some options or paths) list of files is
saved to text file, and Your favorite text editor is launched. You can
edit names or paths in this file, and after You save changes and quit
from editor, this changes are applied.

``irename`` use by default editor set in environment variables:
``$EDITOR``, or ``$VISUAL`` if the former is empty. If neither of them
aren't set, use ``vim``.

Current stable version
----------------------

0.1.0

Python version
--------------

``irename`` works only with Python 3.3+. Older Python versions are
unsupported.

Usage
-----

Everything is in help :) Just execute:

::

    irename --help

Look at result:

::

    % irename --help

    usage: irename [-h] [--editor EDITOR] [--editor-arguments ARGUMENTS]
                   [--verbose] [--interactive] [--force] [--version]
                   [files [files ...]]

    positional arguments:
      files                 files to rename

    optional arguments:
      -h, --help            show this help message and exit
      --editor EDITOR, -e EDITOR
                            Change default editor
      --editor-arguments ARGUMENTS, -c ARGUMENTS
                            Pass additional arguments to editor
      --verbose, -v         Be verbose
      --interactive, -i     Ask before every rename
      --force, -f           Do not ask if destination file already exists
      --version             show program's version number and exit

Installation
------------

1. Using PIP

``irename`` should work on any platform where
`Python <http://python.org>`__ is available, it means Linux, Windows,
MacOS X etc.

Simplest way is to use Python's built-in package system:

::

    pip3 install irename

2. Using `pipsi <https://github.com/mitsuhiko/pipsi>`__

   pipsi install --python3 irename

3. Using sources

Download sources from
`Github <https://github.com/msztolcman/irename/archive/0.1.0.zip>`__:

::

    wget -O 0.1.0.zip https://github.com/msztolcman/irename/archive/0.1.0.zip

or

::

    curl -o 0.1.0.zip https://github.com/msztolcman/irename/archive/0.1.0.zip

Unpack:

::

    unzip 0.1.0.zip

And install

::

    cd irename-0.1.0
    python3 setup.py install

Voila!

Authors
-------

Marcin Sztolcman marcin@urzenia.net

Contact
-------

If you like or dislike this software, please do not hesitate to tell me
about this me via email (marcin@urzenia.net).

If you find bug or have an idea to enhance this tool, please use
GitHub's `issues <https://github.com/msztolcman/irename/issues>`__.

License
-------

The MIT License (MIT)

Copyright (c) 2016 Marcin Sztolcman

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

ChangeLog
---------

v1.0.0
~~~~~~

-  First public version
