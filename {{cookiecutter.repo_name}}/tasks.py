# -*- coding: utf-8 -*-
import os
import sys
import webbrowser

from invoke import task, run

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')

@task
def test(watch=False, last_failing=False):
    """Run the tests.

    Note: --watch requires pytest-xdist to be installed.
    """
    import pytest
    flake()
    args = []
    if watch:
        args.append('-f')
    if last_failing:
        args.append('--lf')
    retcode = pytest.main(args)
    sys.exit(retcode)

@task
def flake():
    """Run flake8 on codebase."""
    run('flake8 .', echo=True)

@task
def clean():
    run("rm -rf build")
    run("rm -rf dist")
    run("rm -rf {{cookiecutter.repo_name}}.egg-info")
    clean_docs()
    print("Cleaned up.")

@task
def clean_docs():
    run("rm -rf %s" % build_dir, echo=True)

@task
def browse_docs():
    path = os.path.join(build_dir, 'index.html')
    webbrowser.open_new_tab(path)

@task
def docs(clean=False, browse=False, watch=False):
    """Build the docs."""
    if clean:
        clean_docs()
    run("sphinx-build %s %s" % (docs_dir, build_dir), echo=True)
    if browse:
        browse_docs()
    if watch:
        watch_docs()

@task
def watch_docs():
    """Run build the docs when a file changes."""
    try:
        import sphinx_autobuild  # noqa
    except ImportError:
        print('ERROR: watch task requires the sphinx_autobuild package.')
        print('Install it with:')
        print('    pip install sphinx-autobuild')
        sys.exit(1)
    run('sphinx-autobuild {0} {1} --watch {2}'.format(
        docs_dir, build_dir, 'marshmallow'), echo=True, pty=True)

@task
def readme(browse=False):
    run('rst2html.py README.rst > README.html')
    if browse:
        webbrowser.open_new_tab('README.html')

@task
def publish(test=False):
    """Publish to the cheeseshop."""
    clean()
    if test:
        run('python setup.py register -r test sdist bdist_wheel', echo=True)
        run('twine upload dist/* -r test', echo=True)
    else:
        run('python setup.py register sdist bdist_wheel', echo=True)
        run('twine upload dist/*', echo=True)
