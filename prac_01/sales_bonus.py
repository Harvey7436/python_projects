"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
import salary as salary

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales*0.1
    salary = sales+bonus
    print(f"Your bonus is{bonus:.2f},Your salary is {salary}")
else:
    sales >= 1000
    bonus = sales*0.15
    salary = sales + bonus
    print(f"Your bonus is{bonus:.2f},Your salary is {salary}")