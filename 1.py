name = input("What is your name?: ")
age = int(input("And your age?: "))
year = 2020 - age + 100

msg = "Your name is {} and you are {} years old. In the year {} you turn 100\n".format(name, age, year)

print(msg)

n = int(input("Give me another number: "))

print(msg * n)