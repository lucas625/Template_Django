# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Script for generating allowed hosts env value."""


import argparse

DESCRIPTION = 'Generates the allowed hosts variable value'
PRODUCTION_HELP_MSG = 'Enables/disables host production environment'


def main():
    """Generates the allowed hosts variable value."""
    parse = argparse.ArgumentParser(description=DESCRIPTION)
    parse.add_argument(
        '--production',
        dest='production',
        action='store_true',
        default=False,
        help=PRODUCTION_HELP_MSG)

    args = parse.parse_args()
    allowed_hosts_address = '[*]'

    if args.production:
        allowed_hosts_address = '[]'

    print(allowed_hosts_address)


if __name__ == '__main__':
    main()
