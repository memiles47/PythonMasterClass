__author__ = 'Michael E Miles'

# add to the program below so that if it finds a meal without spam
# it prints out each of the ingredients of the meal.
# You will need to set up the menu as did in the lines 7 -15 below

menu = list()
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "Sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])

for meal in menu:
    if "spam" not in meal:
        for item in meal:
            print(item)
