
print('**************************************')
print('**   Welcome to the Snakes Cafe!    **')
print('**    Please See Our Menu Below     **')
print('** To quit at any time, type "Quit" **')
print('**************************************')



appetizers = ['Wings', 'Cookies', 'Spring Rolls']
entrees = ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden']
desserts = ['Ice Cream', 'Cake', 'Pie']
drinks = ['Coffee', 'Tea', 'Unicorn Tears']

print('')
print(""" Appetizers """)
print("----------")
for appetizer in appetizers:
    print(appetizer)

print('')
print(""" Entrees """)
print("----------")
for entree in entrees:
    print(entree)

print('')
print(""" Desserts """)
print("----------")
for dessert in desserts:
    print(dessert)

print('')
print(""" Drinks """)
print("----------")

for drink in drinks:
    print(drink)

items = {}

print('***********************************')
print('** What would you like to order? **')
print('***********************************')
while True:
    order = input('> ').capitalize()
    plural_order = 'orders'
    singular_order = 'order'
    have = 'have'
    has = 'has'
    if order == 'Quit':
        break
    elif order not in desserts + appetizers + drinks + entrees:
        print("Sorry that's not available from our menu")
        continue
    elif order not in items:
        items[order] = 0

    items[order] += 1
    if items[order] > 1:
        plural_order = plural_order
        have = have
    else:
        plural_order = singular_order
        have = has
    print(f"** {items[order]} {plural_order} of {order} {have} been added to your meal**")

