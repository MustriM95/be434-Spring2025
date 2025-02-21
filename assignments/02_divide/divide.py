#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-21
Purpose: Add Your Purpose
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('INT',
                        metavar='INT',
                        help='Numbers to divide',
                        nargs=2, 
                        type = int)



    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    n1 = args.INT[0]
    n2= args.INT[1]
    if n2 == 0:
        print("error: Cannot divide by zero, dum-dum!")
    else:
        div = n1/n2
        print(n1, "/", n2, "=", div)
              


# --------------------------------------------------
if __name__ == '__main__':
    main()
