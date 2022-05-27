#!/usr/bin/env python

import os
import re
import sys
from setuptools import setup, find_packages

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()

packages = []

requires = ["requests", "six"]


with open("onedep_biocuration/__init__.py", "r") as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("Cannot find version information")


setup(
    name="onedep_biocuration_api",
    version=version,
    description="wwPDB OneDep Biocuration Web Service API.",
    long_description="See:  http://wwpdb.org/",
    author="wwPDB OneDep Development Team",
    author_email="john.westbrook@rcsb.org",
    url="http://wwpdb.org/",
    #
    license="Apache 2.0",
    zip_safe=False,
    classifiers=(
        "Development Status :: 3 - Alpha",
        # 'Development Status :: 5 - Production/Stable',
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ),
    entry_points={
        "console_scripts": [
            "onedep_request=onedep_biocuration.cli.biocuration_cli:run",
        ]
    },
    #
    install_requires=["requests", "six"],
    packages=find_packages(exclude=["onedep_biocuration.tests", "tests.*"]),
    package_data={
        # If any package contains *.md or *.rst files, include them:
        "": ["*.md", "*.rst"],
    },
    #
    test_suite="tests",
    tests_require=[],
    #
    # Not configured ...
    extras_require={
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
)
