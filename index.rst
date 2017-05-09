python_cli_template
===================

Cookiecutter template for a Python command line script.

Remember, when creating a cli program with this template, to:

 * Fill in all your requirements in requirements.txt
 * If you want a 'bin' script to be created by pip, enable the entry_points in setup.py
 * Think about how you want to solve logging. The template has an command line option for a config file and will log to stdout when it's not set
 * If you add more packages (subdirectories) than the one you create your project for, add them to the packages in setup.py
 * Write **tests** for you software and put them in tests/
 * **Document** your project.
  * Write inline documentation to describe your classes and methods
  * Write a readme (./README.rst)
  * Write (a) usage example(s) (./USAGE.rst)
  * Keep a (global) changelog in ./HISTORY.rst


Development Requirements
------------------------

These utilities / libraries are needed to start developing on with this template.

 * curl
 * make
 * cookiecutter
 * virtualwrapper
 * sphinx
 * setuptools


