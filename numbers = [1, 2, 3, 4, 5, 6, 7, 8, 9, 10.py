numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaters= []
for number in numbers:
    if number > 0:
        squaters.append(number * number * number)
print(squaters)

#zadanie 2

list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
for number in list:
    if number == 0:
        print(number) moze to TimeoutError

#zadanie 2a

numbers = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
for number in numbers:
    if number != 0:
        print(number) drugi raz   

# no i mozna jeszcze: zera = [number for number in numbers if number == 0]      