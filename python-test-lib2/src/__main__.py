from com.jpmorgan.pk.service.httpService import HttpService
#from com.jpmorgan.pk.domain.employee import Employee

'''
Created on 22 Mar 2020

@author: pankaj.pankasin
'''
def mainBefore():
    httpService = HttpService.getInstance()
    employee = httpService.invokeService('XXX')
    print(employee.default_age)
    #print(getattr(e,'emp_age')) #'emp_age' is available in class with values = 30 
    #util.printText('Exiting mainBefore function..')
        
if __name__ == '__main__':
    mainBefore()