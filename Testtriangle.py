# -*- coding: utf-8 -*-
"""
Updated Sep 21, 2022
The primary goal of this file is to demonstrate a simple unittest implementation
@author: amrutha 
"""

import unittest

from triangle import classifyTriangle


class Testtriangle(unittest.TestCase):


    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')
    
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(13, 12, 5), 'Right')

    def testRightTriangleD(self): 
        self.assertEqual(classifyTriangle(8, 6, 10), 'Right')

    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral')
    
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 3, 2),'Isoceles')
    
    def testIsocelesTriangleB(self):     
        self.assertEqual(classifyTriangle(4, 6, 6),'Isoceles')
    
    def testIsocelesTriangleC(self): 
        self.assertEqual(classifyTriangle(6, 4, 6),'Isoceles')
    
    def testIsocelesTriangleD(self): 
        self.assertEqual(classifyTriangle(6, 6, 4),'Isoceles')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(10, 15, 12),'Scalene')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1, -1, -1),'InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201, 201, 201),'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle("200", "0", "0"),'InvalidInput')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(5, 1, 1),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 5, 1),'NotATriangle')

    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1, 1, 5),'NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()