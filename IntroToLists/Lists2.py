__author__ = 'Michael E Miles'

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
    if not "spam" in meal:
        print(meal)
