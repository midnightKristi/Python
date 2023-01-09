# Generated by Medikit 0.7.5 on 2020-04-30.
# All changes will be overriden.
# Edit Projectfile and run “make update” (or “medikit update”) to regenerate.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

# Get the classifiers from the classifiers file
tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))
try:
    with open(path.join(here, 'classifiers.txt'), encoding='utf-8') as f:
        classifiers = tolines(f.read())
except:
    classifiers = []

version_ns = {}
try:
    execfile(path.join(here, 'bonobo/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    author='Romain Dorgueil',
    author_email='romain@dorgueil.net',
    data_files=[('share/jupyter/nbextensions/bonobo-jupyter', [
        'bonobo/contrib/jupyter/static/extension.js',
        'bonobo/contrib/jupyter/static/index.js',
        'bonobo/contrib/jupyter/static/index.js.map'
    ])],
    description=
    ('Bonobo, a simple, modern and atomic extract-transform-load toolkit for '
     'python 3.5+.'),
    license='Apache License, Version 2.0',
    name='bonobo',
    python_requires='>=3.5',
    version=version,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=[
        'cached-property ~= 1.5', 'fs ~= 2.4', 'graphviz ~= 0.13',
        'jinja2 ~= 2.10', 'mondrian ~= 0.8', 'packaging ~= 20.3',
        'psutil ~= 5.7', 'python-slugify ~= 4.0.0', 'requests ~= 2.23',
        'stevedore ~= 1.32', 'whistle ~= 1.0'
    ],
    extras_require={
        'dev': [
            'cookiecutter >= 1.7, < 1.8', 'coverage ~= 4.5', 'pytest ~= 4.6',
            'pytest-cov ~= 2.7', 'pytest-timeout >= 1, < 2', 'sphinx ~= 1.7',
            'sphinx-sitemap >= 2.1, < 2.2'
        ],
        'docker': ['bonobo-docker >= 0.6, < 0.8'],
        'jupyter': ['ipywidgets ~= 6.0', 'jupyter ~= 1.0'],
        'sqlalchemy': ['bonobo-sqlalchemy >= 0.6, < 0.8']
    },
    entry_points={
        'bonobo.commands': [
            'convert = bonobo.commands.convert:ConvertCommand',
            'download = bonobo.commands.download:DownloadCommand',
            'examples = bonobo.commands.examples:ExamplesCommand',
            'init = bonobo.commands.init:InitCommand',
            'inspect = bonobo.commands.inspect:InspectCommand',
            'run = bonobo.commands.run:RunCommand',
            'version = bonobo.commands.version:VersionCommand'
        ],
        'console_scripts': ['bonobo = bonobo.commands:entrypoint']
    },
    url='https://www.bonobo-project.org/',
    download_url='https://github.com/python-bonobo/bonobo/tarball/{version}'.
    format(version=version),
)