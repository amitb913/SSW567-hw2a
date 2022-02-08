# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    # test case: isosceles
    def testIsosceles(self):
        self.assertEqual(classifyTriangle(5,5,8), 'Isosceles', '5,5,8 is an Isosceles triangle')
        
    # test case: scalene
    def testScalene(self):
        self.assertEqual(classifyTriangle(7,4,2), 'Scalene', '7,4,2 is a Scalene triangle')
    
    # test case: is a triangle
    def testValidTriangleA(self):
        self.assertEqual(classifyTriangle(4,1,8), 'NotATriangle', '4,1,8 is not a valid triangle')
    
    # test case: is a triangle when c is not the largest number
    def testValidTriangleB(self):
        self.assertNotEquals(classifyTriangle(8,3,6), 'NotATriangle', '4,1,8 is not a valid triangle')
    
    # test case: valid input over 200
    def testValidInputsA(self):
        self.assertEquals(classifyTriangle(250, 10, 199), 'InvalidInput', 'One or more inputs is out of bounds (over 200)')
    
    # test valid inputs under 0
    def testValidInputsB(self):
        self.assertEquals(classifyTriangle(3, -5, 2), 'InvalidInput', 'One or more inputs is out of bounds (negative)')
    
    # test case: triangle is given non-integer values
    def testNonInts(self):
        self.assertEquals(classifyTriangle(4.6, 3.2, 5.1), 'InvalidInput', 'Non-integer values given')
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

