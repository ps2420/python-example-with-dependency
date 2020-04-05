'''
Created on 26 Mar 2020

@author: pankaj.pankasin
'''
from com2.jpmorgan.pk.util import util
from tornado.web import RequestHandler

class DashboardHandler(RequestHandler):
    def get(self):
        util.printText("inside helloHandler get method")
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("templates/template.html", title="My title", items=items)