#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# File: {{cookiecutter.repo_name}}.py
"""
Main module file

main() will be called by scripts
"""

import logging
import logging.handlers
import logging.config
import json
import argparse

__author__ = '''{{cookiecutter.full_name}} <{{cookiecutter.email}}>'''
__docformat__ = 'plaintext'
__date__ = '''{{cookiecutter.release_date}}'''

# This is the main prefix used for logging
LOGGER_BASENAME = '''{{cookiecutter.repo_name}}'''
LOGGER = logging.getLogger(LOGGER_BASENAME)
LOGGER.setLevel(logging.DEBUG)


def get_arguments():
    """
    This get us the cli arguments.

    Returns the args as parsed from the argsparser.
    """
    # https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(
        description='''{{cookiecutter.project_short_description}}''')
    parser.add_argument('--log-config',
                        '-l',
                        action='store',
                        dest='logger_config',
                        help='The location of the logging config json file',
                        default='')
    parser.add_argument('--log-level',
                        '-L',
                        help='Provide the log level. Defaults to INFO.',
                        dest='log_level',
                        action='store',
                        default='INFO',
                        choices=['DEBUG',
                                 'INFO',
                                 'WARNING',
                                 'ERROR',
                                 'CRITICAL'])

    # examples:
    parser.add_argument('--long', '-s',
                        choices=['a', 'b'],
                        dest='parameter_long',
                        action='store',
                        help='Describe the parameter here',
                        default='a',
                        type=basestring,
                        required=True)
    parser.add_argument('--feature',
                        dest='feature',
                        action='store_true')
    parser.add_argument('--no-feature',
                        dest='feature',
                        action='store_false')
    args = parser.parse_args()
    return args


def setup_logging(args):
    """
    This sets up the logging.

    Needs the args to get the log level supplied
    :param args: The command line arguments
    """
    # This will configure the logging, if the user has set a config file.
    # If there's no config file, logging will default to stdout.
    if args.logger_config:
        # Get the config for the logger. Of course this needs exception
        # catching in case the file is not there and everything. Proper IO
        # handling is not shown here.
        config = json.loads(open(args.logger_config).read())
        # Configure the logger
        logging.config.dictConfig(config)
    else:
        handler = logging.StreamHandler()
        handler.setLevel(args.log_level)
        formatter = logging.Formatter(('%(asctime)s - '
                                       '%(name)s - '
                                       '%(levelname)s - '
                                       '%(message)s'))
        handler.setFormatter(formatter)
        LOGGER.addHandler(handler)


def main():
    """
    Main method.

    This method holds what you want to execute when
    the script is run on command line.
    """
    args = get_arguments()
    setup_logging(args)


if __name__ == '__main__':
    main()
