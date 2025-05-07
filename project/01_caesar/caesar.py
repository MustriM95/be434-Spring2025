#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-05-07
Purpose: caesar shift
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='caesar shift',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift',
                        metavar='NUMBER',
                        type=int,
                        default=3)
    
    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag',
                        action='store_true',
                        default=False)
    
    parser.add_argument('-o',
                        '--output',
                        metavar='FILE',
                        type=argparse.FileType('w'),
                        help='Output file',
                        default='-')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_l = alpha.lower()

    with open(args.FILE.name, 'r', encoding='utf-8') as f:
        msg = f.read()


    if args.decode == False:
        coded = []
        for l in msg:
            if l in alpha:
                ind = alpha.index(l)
                ind_shift = (ind + args.number) % len(alpha)
                coded.append(alpha[ind_shift])
            elif l in alpha_l:
                ind = alpha_l.index(l)
                ind_shift = (ind + args.number) % len(alpha)
                coded.append(alpha[ind_shift])
            else:
                coded.append(l)

        args.output.write(''.join(coded))
    else:
        decoded = []
        for l in msg:
            if l in alpha:
                ind = alpha.index(l)
                ind_shift = (ind + len(alpha) - args.number) % len(alpha)
                decoded.append(alpha[ind_shift])
            elif l in alpha_l:
                ind = alpha_l.index(l)
                ind_shift = (ind + len(alpha) - args.number) % len(alpha)
                decoded.append(alpha[ind_shift])
            else:
                decoded.append(l)

        args.output.write(''.join(decoded))




# --------------------------------------------------
if __name__ == '__main__':
    main()
