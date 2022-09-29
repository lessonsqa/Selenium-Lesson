import unittest

class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Called setUpClass")

    def setUp(self):
        print("Called SetUp")

    def test_test1(self):
        print("Called Test 1")

    def test_test2(self):
        print("Called Test 2")
        pass

    def test_test3(self):
        print("Called Test 3")

    def tearDown(self):
        print("Called TeatDown")

    @classmethod
    def tearDownClass(cls):
        print("Called tearDownClass")
