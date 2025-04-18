#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-04-11
Purpose: Parse blast file
"""

import argparse
import pandas as pd
import csv


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Parse blast file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--blasthits',
                        metavar='FILE',
                        help='BLAST -outfmt 6',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-a',
                        '--annotations',
                        metavar='FILE',
                        help='Annotations file',
                        type=argparse.FileType('r'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        help='Output file',
                        type=str,
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Output field delimiter',
                        metavar='DELIM',
                        default=',')

    parser.add_argument('-p',
                        '--pctid',
                        help='Minimum percent identity',
                        metavar='PCTID',
                        default=0.0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    ann = pd.read_csv(args.annotations,  header=0)

    blast = pd.read_csv(args.blasthits, usecols=[0, 2], header=None)
    blast.columns = ["seq_id", 'pident']

    ann = ann.merge(blast, on='seq_id')
    filt = ann[ann['pident'] >= float(args.pctid)]

    out = filt[["seq_id", 'pident', 'depth', 'lat_lon']]
    out = out.rename(columns={'seq_id': 'qseqid'})

    out.to_csv(args.outfile, sep=args.delimiter, index=False)

    l_num = len(out)
    print(f"Exported {l_num} to \"{args.outfile}\".")


# --------------------------------------------------
if __name__ == '__main__':
    main()
