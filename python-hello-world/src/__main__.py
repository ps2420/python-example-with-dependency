from com.jpmorgan2.pk.service.httpService import HttpService
from com.jpmorgan2.pk.webrequest.handler.dashboardHandler import DashboardHandler
from com.jpmorgan2.pk.webrequest.handler.pathQuotingHandler import PathQuotingHandler
# from com.jpmorgan2.pk.domain.employee import Employee

from com2.jpmorgan.pk.util import util
from tornado.web import Application, StaticFileHandler, url

import tornado.ioloop
import os, sys 

root = os.path.dirname(__file__)

def make_app():
    return Application(
        [
        ("/dashboard", DashboardHandler),
        (r"/()", tornado.web.StaticFileHandler, {"path": root + '/templates/', "default_filename": "index.html"}),
        (r'/js/(.*)', StaticFileHandler, {'path': root + './static/js'}),
        (r'/css/(.*)', StaticFileHandler, {'path': root + './static/css'}),
        (r'/images/(.*)', StaticFileHandler, {'path': root + './static/images'}),
        (r'/templates/(.*)', StaticFileHandler, {'path': root + './templates'}),
        ("/path/(.*)", PathQuotingHandler),
    ],
        template_path=root,
        static_path=root
    )

def sayHello():
    httpService = HttpService.getInstance()
    employee = httpService.invokeService('XXX')
    print(employee.default_age)
    util.printText('from python-lib folder..')
      
if __name__ == '__main__':
    sayHello()
    app = make_app()
    app.listen(8889)
    tornado.ioloop.IOLoop.current().start()
