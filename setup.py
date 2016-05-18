#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-bpatheme',
    version='0.1',
    description='',
    license='AGPL3',
    author='CCG, Murdoch University',
    author_email='tech@ccg.murdoch.edu.au',
    url='https://github.com/muccg/ckanext-bpatheme/',
    namespace_packages=['ckanext'],
    packages=['ckanext.bpatheme'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        bpa_theme = ckanext.bpatheme.plugins:CustomTheme
    """
)
