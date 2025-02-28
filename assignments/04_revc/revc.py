#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-28
Purpose: Reverse complement
"""

import argparse
import os.path
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Reverse complement',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input sequence or file')

    return parser.parse_args()
# --------------------------------------------------


def main():
    """Main Function"""
    args = get_args()
    dna = args.DNA

    if os.path.isfile(dna):
        with open(dna, 'r', encoding='utf-8') as f:
            dna_str = f.readline()
    else:
        dna_str = dna

    rev_dna = dna_str[::-1]
    revc = rev_dna.replace('A', 'At')
    revc = revc.replace('T', 'Ta')
    revc = revc.replace('G', 'Gc')
    revc = revc.replace('C', 'Cg')
    revc = re.sub('[A-Z]', '', revc)
    print(revc.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
