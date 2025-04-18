#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-18
Purpose: Find conserved sequence
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find conserved sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input file',
                        type=argparse.FileType('r'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = args.FILE.read().splitlines()

    out = []
    for i in range(0, len(seqs[0])):
        bases = []
        bases = [[l[i] for l in seqs]]
        conserved = all(j == bases[0][0] for j in bases[0])
        if conserved:
            out.append('|')
        else:
            out.append('X')
    for seq in seqs:
        print(seq)

    print(''.join(out))


# --------------------------------------------------
if __name__ == '__main__':
    main()
