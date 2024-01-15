def solve(meal_cost, tip_percent, tax_percent):
    total = meal_cost + (meal_cost*tip_percent/100) + (meal_cost*tax_percent/100)
    print(round(total))
