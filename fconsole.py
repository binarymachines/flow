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


def resolve_value(value_subtree):

    for node in value_subtree.iter_subtrees():
        if node.data == 'number':
            return int(node.children[0].value)

        if node.data == 'string':
            return node.children[0].value


def resolve_var(variable_subtree):
    
    varname = None
    for node in variable_subtree.iter_subtrees_topdown():
        if node.data == 'name':
            varname = node.children[0].value

        if node.data == 'value':
            #value_node = node.children[0]            
            value = resolve_value(node)
            
    return {
        varname: value
    }


def explore(parse_tree):
    print(dir(parse_tree))

    expression_buffer = []
    symbol_table = {}

    for node in parse_tree.iter_subtrees_topdown():
        if node.data == 'form':
            print('### start-of-form')

        if node.data == 'variable':
            
            symbol_table.update(resolve_var(node))
            print(f'### Symbol table updated: {resolve_var(node)}')

            #print(node.scan_values())

        if node.data == 'expression':
            print(f'### found an expression with {len(node.children)} child nodes.')

            for child in node.children:
                if child.data == 'name':
                    expression_buffer.append(child.children[0])

                if child.data == 'operator':
                    expression_buffer.append(child.children[0])

                if child.data == 'number':
                    expression_buffer.append(child.children[0])

                if child.data == 'expression':
                    continue

    print(f'### symbols:')
    print(common.jsonpretty(symbol_table))

    pylines = []
    locals = []
    for key, value in symbol_table.items():
        locals.append(f'{key} = {value}')

    #pylines.append(f'{" ".join(expression_buffer)})')
    pystmt = ' '.join(expression_buffer)
    print(pystmt)

    print('### can I get a witness?')
    print(eval(pystmt, {}, symbol_table))

    


def main(args):
    
    grammarfile_name = args['<grammar_file>']
    flow_grammar = None

    with open(grammarfile_name, 'r') as f:
        flow_grammar = f.read()

    parser = Lark(flow_grammar, parser='lalr', debug=True)
    parse_tree = None

    if args['--flowcode']:
        codefile = args['<code_file>']
        with open(codefile, 'r') as f:
            code = f.read()
            parse_tree = parser.parse(code)

        print(parse_tree.pretty('\t'))
        explore(parse_tree)


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)