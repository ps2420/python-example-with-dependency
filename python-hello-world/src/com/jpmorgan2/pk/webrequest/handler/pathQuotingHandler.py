'''
Created on 26 Mar 2020

@author: pankaj.pankasin
'''

from com2.jpmorgan.pk.util import util
from tornado.web import RequestHandler

class PathQuotingHandler(RequestHandler):
    def get(self, path):
        util.printText("Request successfully received in PathOutgoingHandler..")
        self.write(path)