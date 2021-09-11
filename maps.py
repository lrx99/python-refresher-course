store = [('Burger', 5),
         ('Fries', 6),
         ('coke', 1)]

to_euros = lambda data: (data[0], data[1]*0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)