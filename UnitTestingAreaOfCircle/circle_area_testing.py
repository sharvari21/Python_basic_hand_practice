
import unittest
import area_of_circle

class CircleTesting(unittest.TestCase):
    def testRadius(self):  # TestCase 1
        temp_radius = 4
        result = area_of_circle.areaCircle(temp_radius)
        #Important line
        self.assertAlmostEqual(result,50.24)
        # THe above line checks your result from function is equal to 
        # the manully given result, 
        # if yes then it says test passed 
        # if no then it says test failed
        
    def testRadiusTwo(self): # TestCase 2
        temp_radius = 101
        result = area_of_circle.areaCircle(temp_radius)
        self.assertAlmostEqual(result,32031.14)
        
if __name__ == "__main__":
    unittest.main()
