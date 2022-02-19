Name_Surname = input("Please enter your First and Second Name \n")
name = ""
surname = ""
count = 0
for i in Name_Surname:
    if i == " ":
        name += i
        break
    name += i
Name_Surname = Name_Surname.replace(name, "")
for i in Name_Surname:
    if i == " ":
        break
    surname += i
    print(surname)

print(surname + " " + name)