## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
month_salary = yearly_salary / 12
month_portion_saved = month_salary * portion_saved
r = 0.05
months = 0

def calc_amount_saved (current_amount_saved, month_portion_saved, r):
    return month_portion_saved + current_amount_saved * (r/12)

while amount_saved < cost_of_dream_home * portion_down_payment:
    amount_saved += calc_amount_saved(amount_saved, month_portion_saved, r)
    months+=1

print("Number of months:", months)
###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
# yearly_salary=112000, portion_saved=.17, cost_of_dream_home=750000 → months = 97
# yearly_salary=65000,  portion_saved=.20, cost_of_dream_home=400000 → months = 79
# yearly_salary=350000, portion_saved=.30, cost_of_dream_home=10000000 → months = 189