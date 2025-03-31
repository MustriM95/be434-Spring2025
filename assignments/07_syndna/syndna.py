#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-03-28
Purpose: Create synthetic DNA
"""

import argparse
import random
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create synthetic DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        default='out.fa',
                        type=argparse.FileType('wt'),
                        metavar='str')

    parser.add_argument('-t', 
                        '--seqtype',
                        metavar='str',
                        help='DNA or RNA',
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        metavar='int',
                        help='Number of sequences to generate',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        metavar='int',
                        help='Minimum length',
                        type=int,
                        default=50)
    
    parser.add_argument('-x',
                        '--maxlen',
                        metavar='int',
                        help='Maximum length',
                        type=int,
                        default=75)

    parser.add_argument('-p',
                        '--pctgc',
                        metavar='float',
                        help='Percent GC',
                        type=float,
                        default=0.5)

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        help='Random seed',
                        default='None')

    return parser.parse_args()



def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""

    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc/2)*max_len)
    num_at = int(((1-pctgc)/2)*max_len)
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    parser = argparse.ArgumentParser(
        description='Create synthetic DNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    args = get_args()
    random.seed(args.seed)

    cwd = os.getcwd()

    if not 0 < args.pctgc < 1:
       parser.error(f'--pctgc "{float(args.pctgc)}" must be between 0 and 1')
       SystemExit

    if args.seqtype not in ("rna", "dna"):
        parser.error(f'--seqtype"{args.seqtype}" must be dna or rna')
        SystemExit

    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for i in range(1, args.numseqs + 1):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = random.sample(pool, k=seq_len)
        seq = ''.join(seq)
        args.outfile.write(f">{i} \n {seq} \n")

    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to "{args.outfile.name}".')

# --------------------------------------------------
if __name__ == '__main__':
    main()
