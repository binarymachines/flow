#!/usr/bin/env python

import os, sys
from abc import ABC



class Field(ABC):
    def __init__(self):
        pass


class Formula(Field):
    def __init__(self):
        pass


class Variable(Field):
    def __init__(self):
        pass


class Assertion(Field):
    def __init__(self):
        pass


class DataForm(object):
    '''a top-level variable holding persistent state
    '''

    def __init__(self, name: str):
        self.name = name
        self.fields = {}


class DataFormBuilder(object):
    def __init__(self):
        pass


class FormDelta(object):
    def __init__(self, form_name: str, field_name: str, value: object):
        pass



class FormAction(object):
    def __init__(self, form_name: str, field_Name: str, value: object):
        pass



class FormEngine(object):
    def __init__(self):
        self._forms = {}


    def add_form(self, name, form_spec):
        pass


    def modify(self, form_name:str, form_field:str, value: object):
        '''
        --this will produce a FormDelta object which will propagate down the tree
        --for setting values internally and generating outputs
        --the FormEngine will issue appropriate commands to the Renderer based on the modification

        '''
        pass

    
    def input(self, form_name: str, form_field: str, value: object):
        '''
        -- this will  produce a FormAction which will propagate "up" from the bottom
        and result in updating the form's internal model
        '''
        pass


    


