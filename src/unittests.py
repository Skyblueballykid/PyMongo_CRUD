import unittest
from src.FlaskAPI import hello


class TestMongoCRUD(unittest.TestCase):

    def TestCREATE(self):
        self.assertTrue(hello.equals("hello world"))


if __name__ == "__main__":
    unittest.main()
