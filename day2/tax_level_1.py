name=input("enter the employee name:")
employee_id=int(input("enter employee id:"))
employee_salary=int(input("enter the basic employee salary: "))
special_allowance=int(input("enter the special allowance offered:"))
bonus_percentage=float(input("enter the bonus percentage:"))

gross_monthly_salary = employee_salary+special_allowance
gross_anual_salary = (gross_monthly_salary*12) + bonus_percentage

print("the name of the employee is:",name)
print("the employee id is:",employee_id)
print("the basic employee salary is:",employee_salary)
print("the special allowance offered is:",special_allowance)
print("the bonus percentage is:",bonus_percentage)
print("the gross monthly salary of an employee is:",gross_monthly_salary)
print("the anual gross salary of an employee is:",gross_anual_salary)
