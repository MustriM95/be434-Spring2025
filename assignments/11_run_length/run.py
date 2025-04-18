#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-18
Purpose: Run length
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run length',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        help='DNA text or file')

    return parser.parse_args()

def run_length(seq):
    """Function translates DNA sequence to encoded format"""


    seq = seq + ' '
    run = []
    i = 0
    j = 1
    for b in seq:
        if i == 0:
            temp = b
            i += 1
        else:
            if b == temp:
                j += 1
            else:
                if j == 1:
                    run.append(f'{temp}')
                else:
                    run.append(f'{temp}{j}')
                temp = b
                j = 1

    return print(''.join(run))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if os.path.isfile(args.str):
        with open(args.str, 'r', encoding='utf-8') as f:
            dna = f.read().splitlines()

            list(map(run_length, dna))
    else:
        dna = args.str
        dna = ''.join(dna)

        run_length(dna)


# --------------------------------------------------
if __name__ == '__main__':
    main()
