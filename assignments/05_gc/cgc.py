#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-03-14
Purpose: GC conent
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='GC conent',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        help='Input sequence file')

    return parser.parse_args()


def gc_calc(s):
    """Calculate GC content"""
    total = len(s)
    c_cont = s.count("C")
    g_cont = s.count("G")

    gc = 100*(g_cont+c_cont)/total

    return gc


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    dna = args.FILE

    seq_id = []
    seq = []
    fasta = []

    if os.path.isfile(dna):
        with open(dna, 'r', encoding='utf-8') as f:
            i = 1
            fasta = f.read().replace('\n', '')
    else:
        print("File not found")

    data = fasta.split(">")
    data = data[1:]

    seq_num = int(len(data))
    for i in range(0, seq_num):
        seq_id.append(data[i][0:13])
    for i in range(0, seq_num):
        seq.append(data[i][13:])
    seq_gc = []

    for i in range(0, seq_num):
        seq_gc.append(gc_calc(seq[i]))

    gc_max = max(seq_gc)
    max_index = seq_gc.index(gc_max)

    print(seq_id[max_index], f'{gc_max:.6}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
