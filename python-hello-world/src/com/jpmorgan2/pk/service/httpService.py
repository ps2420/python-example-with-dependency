from com.jpmorgan2.pk.domain.employee import Employee
from com2.jpmorgan.pk.util import util

class HttpService:
    __instance = None
   
    @staticmethod 
    def getInstance():
        """ Static access method. """
        if HttpService.__instance == None:
            HttpService.__instance = HttpService()
        return HttpService.__instance
   
    def __init__(self):
        """ Virtually private constructor. """
        if HttpService.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            HttpService.__instance = self
         
    
    def invokeService(self, arg1):
        util.printText('http-service-invoked with argument :: ' + arg1) 
        e = Employee()
        return e   