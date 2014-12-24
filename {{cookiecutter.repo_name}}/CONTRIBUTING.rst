Contributing guidelines
=======================

In General
----------

- `PEP 8`_, when sensible.
- Test ruthlessly. Write docs for new features.
- Even more important than Test-Driven Development--*Human-Driven Development*.

.. _`PEP 8`: http://www.python.org/dev/peps/pep-0008/


In Particular
-------------

Questions, Feature Requests, Bug Reports, and Feedback. . .
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

. . .should all be reported on the `Github Issue Tracker`_ .

.. _`Github Issue Tracker`: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/issues?state=open

Setting Up for Local Development
++++++++++++++++++++++++++++++++

1. Fork `{{cookiecutter.project_name}}`_ on Github.
2. Clone your fork::

    $ git clone git@github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}.git

3. Install development requirements. It is highly recommended that you use a virtualenv. ::

    # After activating your virtualenv
    $ pip install -r dev-requirements.txt

3. Install {{cookiecutter.repo_name}} in develop mode. ::

   $ pip install -e .

Git Branch Structure
++++++++++++++++++++

{{cookiecutter.repo_name}} abides by the following branching model:


``dev``
    Current development branch. **New features should branch off here**.

``pypi``
    Current production release on PyPI.

``X.Y-line``
    Maintenance branch for release ``X.Y``. **Bug fixes should be sent to the most recent release branch.**. The maintainer will forward-port the fix to ``dev``. Note: exceptions may be made for bug fixes that introduce large code changes.

**Always make a new branch for your work**, no matter how small. Also, **do not put unrelated changes in the same branch or pull request**. This makes it more difficult to merge your changes.


Pull Requests
++++++++++++++

1. Create a new local branch. ::

    $ git checkout -b name-of-feature

2. Commit your changes. Write `good commit messages <http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>`_.

    $ git commit -m "Detailed commit message"
    $ git push origin name-of-feature

2. Before submitting a pull request, check the following:

- If the pull request adds functionality, it should be tested and the docs should be updated.
- The pull request should work on Python 2.6, 2.7, 3.3, and PyPy. Use ``tox`` to verify that it does.

3. Submit a pull request to the ``dev`` branch.

Running tests
+++++++++++++

To run all the tests: ::

    $ invoke test

To run tests on Python 2.6, 2.7, and 3.3 virtual environents: ::

    $ tox


Documentation
+++++++++++++

Contributions to the documentation are welcome. Documentation is written in `reStructured Text`_ (rST). A quick rST reference can be found `here <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_. Builds are powered by Sphinx_.

To install the packages for building the docs: ::

    $ pip install -r docs/requirements.txt

To build the docs: ::

    $ invoke docs -b

The ``-b`` (for "browse") automatically opens up the docs in your browser after building.

.. _Sphinx: http://sphinx.pocoo.org/

.. _`reStructured Text`: http://docutils.sourceforge.net/rst.html

.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/

.. _`{{cookiecutter.project_name}}`: https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}
