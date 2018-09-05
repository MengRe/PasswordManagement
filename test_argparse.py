import argparse
import sys


def parse_argument(argv):
    parse = argparse.ArgumentParser(description='password command line parameter')

    parse.add_argument('-s', '--search', type=str,
                       help='search an account')
    parse.add_argument('-a', '--add', type=str,
                       help='add an account')
    parse.add_argument('-r', '--remove', type=str,
                       help='remove an account')
    parse.add_argument('-c', '--change', type=str,
                       help='change an account')

    return parse.parse_args(argv)


if __name__ == '__main__':
    argv = parse_argument(sys.argv[1:])
    print(argv.search)
    print(argv.add)
    print(argv.remove)
    print(argv.change)
