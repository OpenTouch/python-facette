# Copyright (c) 2014 Alcatel-Lucent Enterprise
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from setuptools import find_packages
from setuptools import setup

long_description = """\
python-facette is a pure python SDK which allows connecting to Facette API.
"""

pkgdir = {'': 'src'}

setup(
    name = 'facette',
    version = '1.0',
    description = 'Facette SDK for Python',
    keywords = 'facette REST API SDK',
    long_description = long_description,
    author = 'Alcatel-Lucent Enterprise Personal Cloud R&D',
    author_email = 'dev@opentouch.net',
    url = 'https://github.com/OpenTouch/python-facette',
    package_dir=pkgdir,
    packages=find_packages('src'),
    platforms = ['All'],
    license = 'Apache 2.0',
)
