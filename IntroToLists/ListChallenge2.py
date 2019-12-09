__author__ = 'Michael E Miles'

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.

# Use a for loop to iterate 'n' times, where n is the number of items in your list.
# Each time around the loop, use next() on you list to print the next item.

# hint: use the len() function rather than counting the number of items in the list.

family = ["Dan", "Virginia", "Rick", "Chris", "Tyra", "Michael", "Diane"]
familyIterable = iter(family)

for i in range(0, len(family)):
    print(next(familyIterable))
