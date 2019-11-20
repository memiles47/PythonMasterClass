__author__ = 'Michael E Miles'
# import PyPDF2 as p2

shoppingList = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']
for item in shoppingList:
    if item == 'spam':
        continue
    print('Buy: {}'.format(item))

print('\n')

for item in shoppingList:
    if item == 'spam':
        break
    print('Buy: {}'.format(item))

meal = ['egg', 'bacon', 'beans', 'sausages']
nastyFoodItem = ''

for item in meal:
    if item == 'spam':
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that, then please")

if nastyFoodItem:
    print("Can't I have anything without spam in it?")

for i in range(0, 100, 7):
    print(i)
    if i != 0 and i % 11 == 0:
        break

for i in range(0, 20):
    if i == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    print(i)
