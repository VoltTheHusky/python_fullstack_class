prices = input("Введите цены: ")
new_prices = [int(sort_prices) for sort_prices in prices.split(',')]
new_prices.sort()
new_prices_max = new_prices.index(max(new_prices))
new_prices_min = new_prices.index(min(new_prices))
new_prices[new_prices_max], new_prices[new_prices_min] = new_prices[new_prices_min], new_prices[new_prices_max]
print(f"Новые цены: {new_prices}")