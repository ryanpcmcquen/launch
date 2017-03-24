#!/usr/bin/env python3
## Increment versions by ryanpcmcquen. For use with semantic versioning (MAJOR.MINOR.PATCH).
from _VERSION_ import VERSION
import argparse

def divide_version (v):
    major, minor, patch = str(v).split('.')
    return {
        'major': major,
        'minor': minor,
        'patch': patch
    }

def add1 (num):
    return str(int(num) + 1)

def increment (ver, type):
    v = divide_version(ver)
    major = add1(v['major']) if (type == 'major') else v['major']
    minor = add1(v['minor']) if (type == 'minor') else v['minor']
    patch = add1(v['patch']) if (type == 'patch') else v['patch']
    return major + '.' + minor + '.' + patch

## Parse command line options:
parser = argparse.ArgumentParser(
    description = 'Given the file _VERSION_.py with a VERSION variable set to MAJOR.MINOR.PATCH (string), this script will calculate increments for semantic versioning.'
)

parser.add_argument(
    '--major',
    version = increment(VERSION, 'major'),
    action = 'version',
    help = 'Increment by Major version.'
)
parser.add_argument(
    '--minor',
    version = increment(VERSION, 'minor'),
    action = 'version',
    help = 'Increment by Minor version.'
)
parser.add_argument(
    '--patch',
    version = increment(VERSION, 'patch'),
    action = 'version',
    help = 'Increment by Patch version.'
)

args = parser.parse_args()
parser.print_help()


