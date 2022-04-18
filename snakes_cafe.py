
print('**************************************')
print('** Welcome to the Snakes Cafe! **')
print('**************************************')

print('What would you like to order?')
print('Type quit to quit at any time')
print('**************************************')

appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

print(""" Appetizers """)

for appetizer in appetizers:
    print(appetizer)

print('**************************************')
print(""" Entrees """)

for entree in entrees:
    print(entree)

print('**************************************')
print(""" Desserts """)

for dessert in desserts:
    print(dessert)

print('**************************************')
print(""" Drinks """)

for drink in drinks:
    print(drink)

items = {}

while True:
    order = input('> ')
    if order == 'quit':
        break
    elif order not in items:
        items[order] = 0

    items[order] += 1
    print(f"** {items[order]} of {order} have been added to your meal**")

