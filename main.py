feet = int(input("Вкажіть відстань у футах - "))
inch = feet * 12
yards = feet * 0.333333333
miles = feet * 0.000189393939
all = [(inch, "Дюймів"), (yards, "Ярдів"), (miles, "Милів")]
for one, two in all:
    print(f"{feet} Футів = {one} {two}")


