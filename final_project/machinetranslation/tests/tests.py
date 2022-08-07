import unittest
from translator import french_to_english, english_to_french

class TestF2E(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        # Test for null
        self.assertNotEqual(french_to_english('null'), 'Null value')        
        # Test Bonjour returns Hello
        self.assertEqual(french_to_english('Bonjour'), 'Hello')




class TestE2F(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        # Test for null
        self.assertNotEqual(english_to_french('null'), 'Null value')  
        # Test Hello returns Bonjour
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        
unittest.main()