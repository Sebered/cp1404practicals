"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

bonus_percent = 0

sales = float(input('Please enter sales: '))
while sales > 0:
    if sales < 1000:
        bonus_percent = 0.1
    elif sales >= 1000:
        bonus_percent = 0.15
    else:
        print('invalid input')
        sales = float(input('Please enter sales: '))
    bonus = sales * bonus_percent
    print(bonus)
    sales = float(input('Please enter sales: '))