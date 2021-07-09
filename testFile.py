import unittest

from FirstTest import game_difficulty, Api_to_dictionary, print_questions, display_ids, get_json


class TestFileName(unittest.TestCase):

    def test_userinput_not_empty(self):
        self.assertNotEqual(game_difficulty(), "")

    def test_userinput_difficulty(self):
        self.assertNotEqual(game_difficulty(), "hard" or "medium" or "easy")

    def test_userinput_negative(self):
        self.assertNotEqual(game_difficulty(), "-1")

    def test_userinput_greaterthan2(self):
        self.assertNotEqual(game_difficulty(), "3")

    def test_displayChoice_isLess(self):
        self.assertLess(display_ids(), "33")

    def test_displayChoice_isGreater(self):
        self.assertGreater(display_ids(), "8")

    def test_displayChoice_isGreaterEqual(self):
        self.assertGreater(display_ids(), "9")

    def test_displayChoice_isLess(self):
        self.assertLessEqual(display_ids(), "32")

    def test_displayIdchoice_isnot_string(self):
        self.assertNotEqual(display_ids(), "entertainment")

    def test_display_ids_stringRep(self):
        self.assertNotEqual(display_ids(), "Art")

        
if __name__ == '__main__':
    unittest.main()
