loop = True
def check_func():
    if num % check == 0:
        print("Check is equal to num\n")
    else:
        print("Check is not equal to num\n")

while loop:

  num = int(input("Give me a number: "))

  check = int(input("Give me a second number: "))



  if num % 2:
     print("its odd")
     check_func()

  elif num % 4 == 0:
      print("Its a multiple of 4")
      check_func()

  else:
     print("its even")
     check_func()
