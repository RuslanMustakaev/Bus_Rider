import itertools

menu = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)

for food, price in zip(menu, prices):
    limit_budget = 30
    if sum(price) <= limit_budget:
        print(*food, sum(price))
