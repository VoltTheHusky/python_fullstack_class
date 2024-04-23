prices = input("Введите цены: ")
new_prices = [int(sort_prices) for sort_prices in prices.split(',')]
new_prices.sort(reverse=True)
print (new_prices)