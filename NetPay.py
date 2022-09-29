import EmployeeClass as ec
import PayrollDeductionClass as pc
 
 
def Main():
    emp = ec.Employee("Jimmy Smith", 58475, "Information Systems", "Developer", 6800)
 
   
    ded1= pc.PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
    ded2= pc.PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
    ded3= pc.PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
    ded4= pc.PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
    ded5= pc.PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

    deductions = [ded1, ded2, ded3, ded4, ded5]

    net_pay = emp.getSalary()

    
    for ded in deductions:
        if pc.PayrollDeduction.getEmployeeID(ded) == emp.getID():
            net_pay -= pc.PayrollDeduction.getCharge(ded)
        

    

 
   
    print("*** Employee Pay ***")
    print("Name:", ec.Employee.getName(emp))
    print("ID Number:", ec.Employee.getID(emp))
    print("Department:", ec.Employee.getDept(emp))
    print("Gross Pay: $", ec.Employee.getSalary(emp), sep="")
    print("Net Pay: $", net_pay)

 
 
 
 
 
 
Main()
