import unittest
from FirstTest import game_difficulty, get_json

class TestFileName(unittest.TestCase):
      def test_userinput_not_empty(self):
          self.assertNotEqual(game_difficulty(), "")
        
      def test_userinput_difficulty(self):
          self.assertEqual(game_difficulty(), "hard" or "medium" or "easy")

      def test_userinput_negative(self):
          self.assertNotEqual(game_difficulty(), "-1")
          
      def test_userinput_greaterthan2(self):
          self.assertEqual()

if __name__ == '__main__':
    unittest.main()
