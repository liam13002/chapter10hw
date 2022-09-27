class Employee:
   
   
    def __init__(self, name, IdNum, dept, title, salary):
        self.__name= name
        self.__IdNum= IdNum
        self.__dept= dept
        self.__title= title
        self.__salary= salary
   
   
    def getName(self):
        return self.__name
   
   
    def getID(self):
        return self.__IdNum
   
   
    def getDept(self):
        return self.__dept
   
   
    def getJobTitle(self):
        return self.__title
   
   
    def getSalary(self):
        return self.__salary
