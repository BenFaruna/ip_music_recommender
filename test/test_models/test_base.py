#!/usr/bin/python3
'''module containing tests for base_model module'''
import unittest
import MySQLdb as sql

from models.base_model import BaseModel
from models.artist import Artist


class TestBaseModel(unittest.TestCase):
    '''test cases for base_model module'''

    def test_object_creation_without_params(self):
        '''test if BaseModel object is created properly from class
        without parameters'''
        a = BaseModel()
        self.assertIsInstance(a, BaseModel)
        self.assertDictEqual(a.__dict__, {})

    def test_object_creation_with_params(self):
        '''test if BaseModel object is created properly from class
        without parameters'''
        a = BaseModel(name='testcase', lifetime='fortest')
        self.assertIsInstance(a, BaseModel)
        self.assertDictEqual(a.__dict__, {
            'name': 'testcase',
            'lifetime': 'fortest'}
            )

    def test_string_representation(self):
        '''test string representation of model objects'''
        a = BaseModel(name='stringrep', time='testing')
        str_rep = "[{}] {}".format(a.__class__.__name__, a.__dict__)
        self.assertEqual(str_rep, str(a))

    def test_dictionary_representation(self):
        '''test dictionary representation of objects'''
        a = BaseModel()
        b = BaseModel(name='not empty', note='contain kwargs')
        self.assertDictEqual(a.to_dict(), a.__dict__)
        self.assertDictEqual(b.to_dict(), b.__dict__)
