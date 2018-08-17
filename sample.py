#!/usr/bin/env python3

import random as rd
import sys
import argparse

def sample(filename, n, header):
    with open(filename) as f:
        if header:
            sys.stdout.write(next(f))
        for l in f:
            if rd.random() < n:
                sys.stdout.write(l)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sample some fraction of a the rows of a file')
    parser.add_argument('filename')
    parser.add_argument('-f','--fraction', type=float,
            help='Fraction of file to be returned', required=True)
    parser.add_argument('--header', dest='header', action='store_true')
    args = vars(parser.parse_args())

    sample(args['filename'], args['fraction'], args['header'])
