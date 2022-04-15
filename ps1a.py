current_savings = 0
r = 0.04

annual_salary = float(input("What is your annual salary? "))
portion_saved = float(input("what portion of your salary will you save? "))
total_cost = float(input("What is the cost of your dream house? ")) 
portion_down_payment = 0.25*total_cost

down_payment = total_cost*portion_down_payment
annual_returns = (current_savings*r)/12
monthly_salary = annual_salary/12
portion_saved = portion_saved*monthly_salary
month = 0


# Calculations 
while (current_savings <= portion_down_payment):
    month += 1
    current_savings += (current_savings * r / 12) + portion_saved
print('Number of months: ' + str(month))