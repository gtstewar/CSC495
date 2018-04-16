import unittest
from GlobalConfig.CardConfig import *
from Pyskell.Language.EnumList import L


class CardConfigTest(unittest.TestCase):
    def test_card_unit(self):
        self.assertEqual(Spade, Spade)
        self.assertEqual(Heart, Heart)
        self.assertEqual(Diamond, Diamond)
        self.assertEqual(Club, Club)
        self.assertTrue(Spade != Heart)
        self.assertTrue(Spade != Diamond)
        self.assertTrue(Diamond != Club)
        self.assertTrue(Heart != Diamond)
        self.assertTrue(Spade < Heart)
        self.assertTrue(Heart < Diamond)
        self.assertTrue(Diamond < Club)
        self.assertTrue(bounds % Diamond == (Spade, Club))
        self.assertTrue(len(L[Spade, ..., Club]) == 4)
        for unit in L[Spade, ..., Club]:
            self.assertTrue(show_unit % unit in (u'\u2660',
                                                 u'\u2665',
                                                 u'\u2666',
                                                 u'\u2663'))

    def test_card_value(self):
        for value in L[(bounds % Ten)[0], ..., (bounds % Ten)[-1]]:
            self.assertTrue(show % value in
                            ('3', '4', '5', '6', '7', '8',
                             '9', '10', 'J', 'Q', 'K', 'A', '2'))

    def test_card(self):
        self.assertTrue(CD(Diamond, King) == CD(Diamond, King))
        self.assertFalse(CD(Diamond, Queen) == CD(Diamond, King))
        # reverted_print(show % C(Diamond, King))
