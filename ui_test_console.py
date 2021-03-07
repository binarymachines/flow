#!/usr/bin/env python

'''
Usage:
    ui_test_console
'''


import os, sys
import jinja2
import docopt

from ui import *

def main(args):
    
    '''
    id="input-group-1"
        label="Email address:"
        label-for="input-1"
        description="We'll never share your email with anyone else.">

    '''
    fg = FormGroup('input-group-1', 
                   'Email address:',
                   label_for='input-1',
                   description='We will not share your email.')

    '''
    id="input-1"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required
        ></b-form-input>
    '''                

    form_input = FormInput('input-1', label='label', required=True, placeholder='Enter email')
    fg.add_component(form_input)

    print(fg.render())


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args)