'''
# คำนวนภาษี
salary = int(input())
tax = 0.07
ot_time = 10
ot_rate = 200

gross_pay = salary + (ot_time * ot_rate)
tax_pay = gross_pay * tax
net_pay = gross_pay - tax_pay

print(f"จ่ายต่อเดือน : {net_pay}") 
'''
def calcurate_salary(salary,ot_time,ot_rate,tax)
    gross_pay = salary + (ot_time * ot_rate)
    tax_pay = gross_pay * tax
    net_pay = gross_pay - tax_pay
    return net_pay,tax_pay,gross_pay

emp_1 = calcurate_salary(,,,)