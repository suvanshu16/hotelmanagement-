import unittest
from items_db import *


class Check(unittest.TestCase):
    regis = Register()
    logi = Login()
    drin = Drinks()
    itm = Item()

    def test_add_user(self):
        result = self.regis.add_user('shyam', 'hari', '98754', 'shyam@gmail.com')
        self.assertTrue(result)

    def test_show_user(self):
        result = self.logi.search_for_user('suvanshu')
        id = result[0][0]
        expected_result = [(id, 'suvanshu', 'suvanshu1', '9842616337', 'suvanshunepal2@gmail.com')]
        self.assertEqual(result, expected_result)

    def test_update_drinks(self):
        result = self.drin.search_drinks('corona')
        id = result[0][0]
        expected_result = self.drin.update_drinks(id, 'corona', 300)
        self.assertTrue(expected_result)

    def test_delete_item(self):
        data = self.itm.search_item('chou')
        id = data[0][0]
        self.assertTrue(self.itm.delete_item(id))

    def test_user_login(self):
        result = self.logi.login_user('suvanshu', 'suvanshu1')
        self.assertEqual(len(result), 1)