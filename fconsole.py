#!/usr/bin/env python

'''
Usage:
    fconsole -g <grammar_file>

'''


import os, sys
import re
import logging
from lark import Lark, logger
from snap import common
import docopt

logger.setLevel(logging.DEBUG)


def main(args):
    
    grammarfile_name = args['<grammar_file>']
    flow_grammar = None

    with open(grammarfile_name, 'r') as f:
        flow_grammar = f.read()

    parse_tree = Lark(flow_grammar, parser='lalr', debug=True)


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)