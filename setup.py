"""
Pip.Services Commons
--------------------

Pip.Services is an open-source library of basic microservices.
Commons basic abstractions portable across variety of languages.

Links
`````

* `website <http://github.com/pip-services/pip-services>`
* `development version <http://github.com/pip-services/pip-services-commons-python>`

"""

from setuptools import setup
from setuptools import find_packages

setup(
    name='pip_services_commons',
    version='2.0.0',
    url='http://github.com/pip-services/pip-services-commons-python',
    license='MIT',
    author='Conceptual Vision Consulting LLC',
    description='Basic portable abstractions for Pip.Services in Python',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    platforms='any',
    install_requires=[
        'iso8601', 'PyYAML', 'pymongo', 'bottle', 'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]    
)
