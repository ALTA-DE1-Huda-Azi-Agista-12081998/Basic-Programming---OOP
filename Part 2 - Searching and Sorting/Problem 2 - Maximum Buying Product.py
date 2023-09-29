def maximum_buy_product(money, product_price):
    if money <= 0 or not product_price:
        return 0

    unique_products = set(product_price)
    sorted_prices = sorted(unique_products)

    total_products = 0
    remaining_money = money

    for price in sorted_prices:
        if price <= remaining_money:
            remaining_money -= price
            total_products += 1
        else:
            break

    return total_products


print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))  # Output: 3
print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000]))  # Output: 4
print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))  # Output: 4
print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))  # Output: 1
print(maximum_buy_product(0, [10000, 30000]))  # Output: 0
