

num1 = int(input("entrer un nombre 1: "))

num2 = int(input("entrer un nombre 2: "))


res = 0

while (True) :
  print("1: +  ")
  print("2: -  ")
  print("3: * : ")
  print("4: / : ")
  print("5: exit")

  operateur = int(input("entrer votre choix de operation : "))

  match(operateur):
    case 1:
      res = num1 + num2
      print(res)
      break
    case 2:
      res = num1 - num2
      print(res)
      break
    case 3:
      res = num1 * num2
      print(res)
      break
    case 4:
      res = num1 / num2
      print(res)
      break
    case 5:
      break




