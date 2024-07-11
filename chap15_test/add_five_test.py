import  unittest 
from add_five import add5

class TestAdd5(unittest.TestCase):
    def testAdd5WithNum(self):
        testNum = 10
        self.assertEqual(add5(testNum), 15)

    def testAdd5WithStr(self):
        testNum = "okla"
        self.assertTrue(isinstance(add5(testNum),ValueError))
        

unittest.main()
