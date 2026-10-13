
num = float(input("entrer un nombre : "))
entier = int(num)

val = entier ** (1/2)
print(val)

while int(val) != val:
  entier -= 1
  val = entier ** (1/2)

print(val)
