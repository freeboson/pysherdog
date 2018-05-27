========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
        | |landscape| |scrutinizer| |codacy| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/pysherdog/badge/?style=flat
    :target: https://readthedocs.org/projects/pysherdog
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/freeboson/pysherdog.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/freeboson/pysherdog

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/freeboson/pysherdog?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/freeboson/pysherdog

.. |requires| image:: https://requires.io/github/freeboson/pysherdog/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/freeboson/pysherdog/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/freeboson/pysherdog/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/freeboson/pysherdog

.. |codecov| image:: https://codecov.io/github/freeboson/pysherdog/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/freeboson/pysherdog

.. |landscape| image:: https://landscape.io/github/freeboson/pysherdog/master/landscape.svg?style=flat
    :target: https://landscape.io/github/freeboson/pysherdog/master
    :alt: Code Quality Status

.. |codacy| image:: https://img.shields.io/codacy/REPLACE_WITH_PROJECT_ID.svg
    :target: https://www.codacy.com/app/freeboson/pysherdog
    :alt: Codacy Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/freeboson/pysherdog/badges/gpa.svg
   :target: https://codeclimate.com/github/freeboson/pysherdog
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/pysherdog.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/pysherdog

.. |commits-since| image:: https://img.shields.io/github/commits-since/freeboson/pysherdog/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/freeboson/pysherdog/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/pysherdog.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/pysherdog

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/pysherdog.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/pysherdog

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/pysherdog.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/pysherdog

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/freeboson/pysherdog/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/freeboson/pysherdog/


.. end-badges

Python API for accessing data on Sherdog.

* Free software: MIT license

Installation
============

::

    pip install pysherdog

Documentation
=============

https://pysherdog.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
