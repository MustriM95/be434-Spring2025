#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-21
Purpose: DNA: count tetranucleotide frequency
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        nargs=1,
                        help='Input DNA sequence',
                        type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = str(args.DNA)
    a_count = dna.count('A')
    c_count = dna.count('C')
    g_count = dna.count('G')
    t_count = dna.count('T')
    print(dna)
    print(a_count, c_count, g_count, t_count)


# --------------------------------------------------
if __name__ == '__main__':
    main()
