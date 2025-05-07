#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-05-07
Purpose: vigenere cipher
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='vigenere cipher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file')

    parser.add_argument('-k',
                        '--keyword',
                        help='A keyword',
                        metavar='KEYWORD',
                        type=str,
                        default='CIPHER')
    
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

    key = args.keyword

    with open(args.FILE.name, 'r', encoding='utf-8') as f:
        msg = f.read()


    if args.decode == False:
        coded = []
        i = 0
        for l in msg:
            if l in alpha:
                ind = alpha.index(l)
                k_l = key[i % len(key)]
                k_ind = alpha.index(k_l)
                ind_shift = (ind + k_ind) % len(alpha)
                coded.append(alpha[ind_shift])
                i += 1
            elif l in alpha_l:
                ind = alpha_l.index(l)
                k_l = key[i % len(key)]
                k_ind = alpha.index(k_l)
                ind_shift = (ind + k_ind) % len(alpha)
                coded.append(alpha[ind_shift])
                i += 1
            else:
                coded.append(l)
                if '\n' in l:
                    i = 0

        args.output.write(''.join(coded))
    else:
        decoded = []
        i = 0
        for l in msg:
            if l in alpha:
                ind = alpha.index(l)
                k_l = key[i % len(key)]
                k_ind = alpha.index(k_l)
                ind_shift = (ind + len(alpha) - k_ind) % len(alpha)
                decoded.append(alpha[ind_shift])
                i += 1
            elif l in alpha_l:
                ind = alpha_l.index(l)
                k_l = key[i % len(key)]
                k_ind = alpha.index(k_l)
                ind_shift = (ind + len(alpha) - k_ind) % len(alpha)
                decoded.append(alpha[ind_shift])
                i += 1
            else:
                decoded.append(l)
                if '\n' in l:
                    i = 0
                
        args.output.write(''.join(decoded))


# --------------------------------------------------
if __name__ == '__main__':
    main()
