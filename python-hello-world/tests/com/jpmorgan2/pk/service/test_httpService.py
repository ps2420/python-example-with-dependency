'''
Created on 4 Apr 2020

@author: pankaj.pankasin
'''
import sys
sys.path.append('/Users/pankaj.pankasin/eclipse-workspace/python-lib/src')

sys.path.insert(0,'/Users/pankaj.pankasin/eclipse-workspace/python-lib/src') 

import unittest
from com.jpmorgan2.pk.service.httpService import HttpService

class TestHttpService(unittest.TestCase):

    httpService = HttpService.getInstance()

    def testInvokeService(self):
        employee = self.httpService.invokeService('XXX')
        print(employee.default_age)
        self.assertEqual(employee.default_age, 50)
        self.assertTrue(employee.default_age, 50)