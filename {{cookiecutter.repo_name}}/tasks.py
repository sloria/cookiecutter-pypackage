# -*- coding: utf-8 -*-
import os
import sys

from invoke import task, run

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')

@task
def test():
    import pytest
    errcode = pytest.main(['tests'])
    sys.exit(errcode)

@task
def watch():
    """Run tests when a file changes. Requires pytest-xdist."""
    import pytest
    errcode = pytest.main(['-f'])
    sys.exit(errcode)

@task
def clean():
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf {{cookiecutter.repo_name}}.egg-info")
    clean_docs()
    print("Cleaned up.")

@task
def clean_docs():
    run("rm -rf %s" % build_dir)

COMMAND_MAP = {
    'darwin': 'open ',
    'linux': 'idle ',
    'win32': '',
}
@task
def browse_docs():
    platform = str(sys.platform).lower()
    cmd = COMMAND_MAP.get(platform)
    if cmd:
        run("{0}{1}".format(cmd, os.path.join(build_dir, 'index.html')))
    else:
        print('Unsure how to open the built file on this operating system.')
        sys.exit(1)

@task
def docs(clean=False, browse=False):
    if clean:
        clean_docs()
    run("sphinx-build %s %s" % (docs_dir, build_dir), pty=True)
    if browse:
        browse_docs()

@task
def readme(browse=False):
    run('rst2html.py README.rst > README.html')

@task
def publish(test=False):
    """Publish to the cheeseshop."""
    try:
        __import__('wheel')
    except ImportError:
        print("wheel required. Run `pip install wheel`.")
        sys.exit(1)
    if test:
        run('python setup.py register -r test sdist bdist_wheel upload -r test')
    else:
        run("python setup.py register sdist bdist_wheel upload")
