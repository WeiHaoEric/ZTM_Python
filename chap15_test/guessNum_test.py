import unittest
from guessNum import checkAns

class GameTest(unittest.TestCase):
    def setUp(self):
        print("=== Initing... ===")

    def testSame(self):
        testNum = 10
        ans = 10
        self.assertEqual(checkAns(testNum, ans), True)
    
    def testDiff(self):
        testNum = 10
        ans = 5
        self.assertEqual(checkAns(testNum, ans), False)

    def tearDown(self) -> None:
        print("Done!")
        return super().tearDown()


unittest.main()