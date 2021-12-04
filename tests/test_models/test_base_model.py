#!/usr/bin/python3
'''
BaseModel test module
'''

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    BaseModel test class
    '''

    def setUp(self):
        '''
        test setup method
        '''

        model = BaseModel()
        model.number = 10
        model.name = "Test"

    def test_save(save):
        '''
        save method test
        '''
        a = model.updated_at
        model.save()
        b = model.updated_at
        self.assertNotEqual(a, b, "Value should not be equal")
