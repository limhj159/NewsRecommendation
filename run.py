from newsrec.train import train
from newsrec.data_preprocess import data_preprocess
from newsrec.evaluate import evaluation

import sys
from typing import List
import argparse


def main(sys_argv: List[str] = None):
    if sys_argv is None:
        sys_argv = sys.argv[1:]

    parser = argparse.ArgumentParser(allow_abbrev=False)
    parser.add_argument('--top', type=str, choices=['training', 'preprocess', 'evaluation'], default='training')
    args = parser.parse_known_args(sys_argv)[0]
    if args.top == 'preprocess':
        data_preprocess()
    elif args.top == 'training':
        train()
    elif args.top == 'evaluation':
        evaluation()


if __name__ == '__main__':
    main()