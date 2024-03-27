books = int (input("Количество книг: "))
stationery = int (input("Количество канцтоваров: "))
toys = int (input("Количество игрушек: "))
volume_toys = toys * 3
volume_stationery = stationery * 1.5
volume_books = books * 2
volume = volume_toys + volume_stationery + volume_books
print (f"Общий объём: {volume} м^3")