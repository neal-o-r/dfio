#!/usr/bin/env python3.6
import pandas as pd
import sys
import argparse
import codecs


def unescaped_str(arg_str):
    return codecs.decode(str(arg_str), 'unicode_escape')


def dfio(fname, delimiter, execute, plot):

    df = pd.read_csv(fname, delimiter=delimiter)
    if plot:
        plot = eval('df.' + execute)
        plot.get_figure().savefig('out.png')
    else:
        sys.stdout.write(str(eval(f'df.{execute}')) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Do dataframe stuff to some data')
    parser.add_argument('filename')
    parser.add_argument('-d', '--delimiter', type=unescaped_str,
                        help='column delimiter', default=',')
    parser.add_argument('-e', '--execute',
                        help='run this command (everything after the df.)')
    parser.add_argument('--plot', dest='plot', action='store_true')
    args = vars(parser.parse_args())

    dfio(args['filename'], args['delimiter'], args['execute'], args['plot'])
