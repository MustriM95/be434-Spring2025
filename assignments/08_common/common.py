#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-03-31
Purpose: Find common
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE',
                        help='Input file 1',
                        type=argparse.FileType('r'),)
    
    parser.add_argument('FILE2',
                        metavar='FILE',
                        help='Input file 2',
                        type=argparse.FileType('r'),)

    parser.add_argument('-o',
                        '--outfile',
                        help='A named string argument',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='-')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file1 = args.FILE1.read().split()
    file2 = args.FILE2.read().split()

    common = list(set(file1).intersection(file2))
    common_str = '\n'.join(common)
    args.outfile.write(f'{common_str}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
