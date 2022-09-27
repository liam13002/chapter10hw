import EmployeeClass as ec
import PayrollDeductionClass as pc
 
 
def Main():
    emp = ec.Employee("Jimmy Smith", 58475, "Information Systems", "Developer", 6800)
 
   
    ded1= pc.PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
    ded2= pc.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
    ded3= pc.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
    ded4= pc.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
    ded5= pc.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)
 
   
    print("*** Employee Pay ***")
    print("Name:", ec.Employee.getName(emp))
    print("ID Number:", ec.Employee.getID(emp))
    print("Department:", ec.Employee.getDept(emp))
    print("Gross Pay: $", float(ec.Employee.getSalary(emp)), sep="")
    print("Net Pay: $", ec.Employee.getSalary(emp)-ded2.getCharge()-ded4.getCharge()-ded5.getCharge(), sep="")
 
 
 
 
 
 
Main()
