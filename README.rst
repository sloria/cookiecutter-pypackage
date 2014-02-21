cookiecutter-pypackage
======================

A python package template, for use with `cookiecutter <https://github.com/audreyr/cookiecutter>`_.

Features
--------

- pytest_ for testing.
- Beautiful Sphinx docs, courtesy of `Kenneth Reitz <https://github.com/kennethreitz/kr-sphinx-themes>`_ .
- ``setup.py`` script with useful commands for publishing to the PyPI.
- wheel_!
- tox and Travis-CI working out-of-the-box.
- Starter ``compat.py`` module for Python 2 and 3 compatibility.


.. _wheel: http://www.python.org/dev/peps/pep-0427/

.. _pytest: http://pytest.org/latest/


To use this template
--------------------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/sloria/cookiecutter-pypackage.git

You will be prompted for basic info (your name, project name, etc.) which will be used in the template.

That's all you need to get started.

Next steps
----------
* Create the Github repo for your project
* Add the repo `Travis-CI`_.
* Add the repo to `ReadTheDocs`_.
* Release your package to the PyPI. Here's a release checklist: https://gist.github.com/sloria/6277657


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/


License
-------

`MIT Licensed <http://sloria.mit-license.org>`_.
