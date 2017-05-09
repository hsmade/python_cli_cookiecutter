#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
version = open('.VERSION').read()

# get the requirements from the requirements.txt
requirements_file = [line.strip()
                     for line in open('requirements.txt').readlines()
                     if line.strip() and not line.startswith('#')]
requirements = requirements_file

# get the test requirements from the test_requirements.txt
test_requirements = [line.strip()
                     for line in open('requirements/testing.txt').readlines()
                     if line.strip() and not line.startswith('#')]

setup(
    name='''{{ cookiecutter.repo_name }}''',
    version=version,
    description='''{{ cookiecutter.project_short_description }}''',
    long_description=readme + '\n\n' + history,
    author='''{{ cookiecutter.full_name }}''',
    author_email='''{{ cookiecutter.email }}''',
    url='''{{ cookiecutter.git_url }}''',
    packages=find_packages(where='.', exclude=('tests', 'hooks')),
    package_dir={'''{{ cookiecutter.repo_name }}''':
                 '''{{ cookiecutter.repo_name }}'''},
    include_package_data=True,
    install_requires=requirements,
    license='''{{ cookiecutter.foss_license }}''',
    zip_safe=False,
    keywords='''{{ cookiecutter.repo_name }}''',
    entry_points={
        'console_scripts': [
            # enable this to automatically generate a script in /usr/local/bin called myscript that points to your
            #  {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name }}:main method
            # 'myscript = {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name }}:main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        '''License :: OSI Approved :: {{ cookiecutter.foss_license }} License''',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    data_files=[
        ('', [
            '.VERSION',
            'LICENSE',
            'AUTHORS.rst',
            'CONTRIBUTING.rst',
            'HISTORY.rst',
            'README.rst',
            'USAGE.rst',
        ]),
    ]
)
