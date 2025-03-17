#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-28
Purpose: Reverse complement
"""

import argparse
#import os.path
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Reverse complement',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # better to lowercase all variables
    parser.add_argument('dna',
                        metavar='dna',
                        help='Input sequence or file')

    # you forgot to check if it is a file, not just a sequence
    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return args
# --------------------------------------------------


def main():
    """Main Function"""
    args = get_args()
    dna = args.dna

    if os.path.isfile(dna):
        with open(dna, 'r', encoding='utf-8') as f:
            dna_str = f.readline()
    else:
        dna_str = dna

    rev_dna = dna_str[::-1]
    # only replaces the first occurance.
#    revc = rev_dna.replace('A', 'T')
#    revc = rev_dna.replace('a', 't')
#    revc = rev_dna.replace('T', 'A')
#    revc = rev_dna.replace('t', 'a')
#    revc = rev_dna.replace('C', 'G')
#    revc = rev_dna.replace('c', 'g')
#    revc = rev_dna.replace('G', 'C')
#    revc = rev_dna.replace('g', 'c')
    #revc = re.sub('[A-Z]', '', revc)

    # a better way is to use a translation table:
    trans = {
        'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A',
        'a': 't', 'c': 'g', 'g': 'c', 't': 'a'
    }

    complement = []
    for base in rev_dna:
        complement.append(trans.get(base, base))

    # you also want to match the case of the sequence
    #print(revc.upper())

    print(''.join(complement))


# --------------------------------------------------
if __name__ == '__main__':
    main()
