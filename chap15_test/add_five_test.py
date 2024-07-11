import  unittest 
from add_five import add5

class TestAdd5(unittest.TestCase):
    def testAdd5WithNum(self):
        testNum = 10
        self.assertEqual(add5(testNum), 15)

    def testAdd5WithStr(self):
        testNum = "okla"
        # === assertion_1 ===
        # self.assertTrue(isinstance(add5(testNum),ValueError))
        
        # === assertion_2=== 
        self.assertIsInstance(add5(testNum), ValueError)

    def testAdd5With0(self):
        testNum = 0
        self.assertEqual(add5(testNum), "[Error]: please provide the val for num.")

      
        
if __name__== "__main__":
    unittest.main()
