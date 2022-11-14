#!/usr/bin/python3
'''module containing test cases for database crud operations'''
import MySQLdb as sql
import unittest

import models

from models.artist import Artist
from models.user import User
from models.track import Track

from models.base_model import Base


class TestDBCrudOperation(unittest.TestCase):
    '''class containing test case for CRUD operations'''

    def setUp(self):
        '''defines database entries for testing'''
        self.__engine = sql.connect(
            host='localhost', user='music_dev',
            database='music_dev_db', password='music_dev_pwd'
            )
        self.__cursor = self.__engine.cursor()
        self.art_obj = Artist(id='ed136ocfbuc2oi83', name='test artist')
        self.art_obj2 = Artist(id='f3rv9ceg2h4invwr', name='test artist 2')
        self.track_obj = Track(
            id='feywiviu42bi238wefub', artist_id='ed136ocfbuc2oi83',
            title='More than test', image_url='https://favicon.jpg')
        self.track_obj2 = Track(
            id='dvyu82793fubw97h2e', artist_id='f3rv9ceg2h4invwr',
            title='testing my way out', image_url='https://favicon.png')
        self.art_obj.add()
        self.art_obj2.add()
        self.track_obj.add()
        self.track_obj2.add()

    def tearDown(self):
        '''clears database entries created during testing'''
        self.track_obj.delete()
        self.track_obj2.delete()
        self.art_obj.delete()
        self.art_obj2.delete()

    def test_get_item_from_db(self):
        '''test the get function of the storage class'''
        a_obj = models.storage.get('Artist', 'ed136ocfbuc2oi83')
        t_obj = models.storage.get('Track', 'feywiviu42bi238wefub')
        self.assertEqual(t_obj.id, self.track_obj.id)
        self.assertEqual(a_obj.id, self.art_obj.id)

    def test_add_items_to_db(self):
        '''test function for adding items to a db'''
        # after_add = self.__cursor.execute("SELECT * FROM artist WHERE id='ed136ocfbuc2oi83';")
        obj = models.storage.get(cls='Artist', id='ed136ocfbuc2oi83')
        self.assertEqual((self.art_obj.id, self.art_obj.name), (obj.id, obj.name))

    def test_delete_item_from_db(self):
        '''test function for deleting items from the database'''
        new_obj = Artist(id='f3g7923gbucew', name='Leavin\' soon')
        new_obj.add()
        new_obj.delete()
        new_obj = models.storage.get('Artist', id='f3g7923gbucew')
        self.assertIsNone(new_obj)
