#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-05-02
Purpose: magic sequence
"""

import argparse
import tabulate as t


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='magic sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        help='Input FASTA file(s)',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-t',
                        '--tablefmt',
                        help='Tabulate table style',
                        metavar='table',
                        type=str,
                        default='plain')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    table = []
    for f in args.FILE:
        seqs = f.read().splitlines()
        seq_num = int(len(seqs)/2)

        if seq_num != 0:
            seq_lens = []
            for i in range(0, seq_num):

                seq_lens.append(len(seqs[1+2*i]))

            min_seq = min(seq_lens)
            max_seq = max(seq_lens)
            avg_sl = sum(seq_lens)/seq_num
        else:
            min_seq = 0
            max_seq = 0
            avg_sl = float(0.0)

        table.append([f.name, min_seq, max_seq, avg_sl, seq_num])

    hds = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    print(t.tabulate(table,
                     headers=hds,
                     tablefmt=args.tablefmt,
                     floatfmt=".2f"))


# --------------------------------------------------
if __name__ == '__main__':
    main()
