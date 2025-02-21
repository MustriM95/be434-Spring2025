#!/usr/bin/env python3
"""
Author : Add your Name <Add your email>
Date   : 2025-02-17
Purpose: Add Your Purpose
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='The greeting',
                        metavar= "str",
                        default='Howdy',
                        action="store", 
                        nargs='?',
                        const="Howdy")

    parser.add_argument('-n',
                        '--name',
                        help='Whom to greet',
                        metavar="str",
                        default='Stranger',
                        action="store", 
                        nargs='?',
                        const="Stranger")
    parser.add_argument('-e',
                        '--excited',
                        help="Include an exclamation point",
                        default=False,
                        action="store_true")


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    g_arg = args.greeting
    n_arg = ""
    if args.excited == True:
        n_arg = args.name + "!"
    else:
        n_arg = args.name + "."
    
    
    print(g_arg + ", " + n_arg )


# --------------------------------------------------
if __name__ == '__main__':
    main()
