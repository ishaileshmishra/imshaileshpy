# https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py
# setup.py is the build script for setuptools.
# It tells setuptools about your package (such
# as the name and version) as well as which code files to include

import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()

requirements = [
    'requests>=2.20.0,<3.0',
    'python-dateutil'
]

setup(
    title="imshaileshpy",
    name="imshaileshpy",
    status="Active",
    type="process",
    created="19 Jun 2023",
    keywords="imshaileshpy-python-package",
    version="1.8.0",
    author="Contentstack",
    author_email="mshaileshr@gmail.com",
    description="Contentstack is a headless CMS with an API-first approach.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishaileshmishra/imshaileshpy",
    packages=['imshaileshpy'],
    license='MIT',
    test_suite='tests',
    install_requires=requirements,
    include_package_data=True,
    universal=1,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    zip_safe=False,
)
