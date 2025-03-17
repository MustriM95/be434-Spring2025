#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-03-16
Purpose: DNA ro RNA
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='DNA ro RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input DNA file')

    parser.add_argument('-o DIR',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        default="out")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna_in = args.FILE
    rna_out = "./" + args.outdir + "/" + dna_in.split("/")[-1]
    out_dir = "./" + args.outdir
    dna = []

    print(rna_out)
    if os.path.isfile(dna_in):
        with open(dna_in, 'r', encoding='utf-8') as f:
            dna = f.read()
    else:
        print("File not found")

    rna = dna.replace('T', 'U')

    if os.path.isdir(out_dir):
        with open(rna_out, "w", encoding='utf-8') as text_file:
            text_file.write(rna)
    else:
        os.makedirs(out_dir)
        with open(rna_out, "w", encoding='utf-8') as text_file:
            text_file.write(rna)


# --------------------------------------------------
if __name__ == '__main__':
    main()
