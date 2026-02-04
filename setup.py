#!/usr/bin/env/python

# -*- coding: utf-8 -*-
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = []

setup(
    name="ckanext-bpaschema",
    version="4.4.8",
    description='''CKAN extension to hold schemas for the Bioplatforms Australian Data Portal''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="AGPL3",
    author="Bioplatforms Australia",
    author_email="help@bioplatforms.com",
    url="https://github.com/BioplatformsAustralia/ckanext-bpaschema",
    namespace_packages=["ckanext"],
    packages=["ckanext.bpaschema"],
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
    package_dir={"ckanext.bpaschema": "ckanext/bpaschema"},
    package_data={
        "ckanext.bpaschema": [
            "*.json",

        ]
    },
    entry_points="""
        [ckan.plugins]
        bpaschema=ckanext.bpaschema.plugin:BpaschemaPlugin

        [babel.extractors]
        ckan = ckan.lib.extract:extract_ckan
    """,
)
