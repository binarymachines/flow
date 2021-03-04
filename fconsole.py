#!/usr/bin/env python

'''
Usage:
    fconsole -g <grammar_file>
    fconsole -g <grammar_file> -f <code_file>

Options:
    -g --grammar  Construct a parse tree from the specified grammar file
    -f --flowcode  Parse the code in the specified file
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
    parse_data = None

    if args['--flowcode']:
        codefile = args['<code_file>']
        with open(codefile, 'r') as f:
            code = f.read()
            parse_data = parse_tree.parse(code)

    print(parse_data)

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)