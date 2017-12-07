print "Dear cook, please report what is on the menu today and how much it should cost!"

menu = {}

while True:
    dish = raw_input("What do we serve today?")
    menu[dish] = raw_input("How much does it cost?")
    new = raw_input("Have you prepared something else? (yes/no)")

    if new == "no":
        break

print "Today we offer:"
for x in menu:
    print x + " " + menu[x] + "eur"

with open("menu.txt", "w+") as menu_file:
    menu_file.write("Today we offer:\n")
    for x in menu:
        menu_file.write(x + " " + menu[x] + "eur\n")