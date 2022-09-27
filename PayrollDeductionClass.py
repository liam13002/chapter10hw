class PayrollDeduction:
   
   
    def __init__(self, desc, date, charge, empID):
        self.__desc= desc
        self.__date= date
        self.__charge= charge
        self.__empID= empID
       
   
    def getDesc(self):
        return self.__desc
   
   
    def getDate(self):
        return self.__date
   
   
    def getCharge(self):
        return self.__charge
   
   
    def getEmployeeID(self):
        return self.__empID
 
