import unittest
from src.FlaskAPI import hello

# http://flask.pocoo.org/docs/1.0/testing/

class TestMongoCRUD(unittest.TestCase):

    def TestCREATE(self):
        self.assertTrue(hello.equals("hello world"))


if __name__ == "__main__":
    unittest.main()
