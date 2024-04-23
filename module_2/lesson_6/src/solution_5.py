prices = input("Введите цены: ")
new_prices = [int(sort_prices) for sort_prices in prices.split(',')]
new_prices.sort()
new_prices[0], new_prices[3] = new_prices[3], new_prices[0]
print(f"Новые цены: {new_prices}")