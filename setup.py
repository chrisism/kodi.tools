from setuptools import setup, find_packages
import io
import os
import sys

import xml.etree.ElementTree as ET

VERSION = '1.0.0'
NAME = 'kodi.tools'
AUTHOR = 'chrisism'
AUTHOR_EMAIL = 'crizizz@gmail.com'
DESCRIPTION = 'Set of kodi addon build tools'
PROJECT_URL = 'https://github.com/chrisism/kodi.tools'
LICENSE = ''
LONG_DESCRIPTION = ''

number_of_arguments = len(sys.argv)
version_parameter = sys.argv[-1]
VERSION = version_parameter.split("=")[1]
sys.argv = sys.argv[0:number_of_arguments-1]

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url=PROJECT_URL,
    license=LICENSE,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6",
    entry_points = '''
        [console_scripts]
        publish-addon=publish:main
        pack-addon=package:main
        update-addon-news=update_news:main
        merge-addon-xml=addon_xml_merger:main
    '''
)