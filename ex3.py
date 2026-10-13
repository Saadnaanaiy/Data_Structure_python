

num = int(input("donner moi votre nombre de jour"))

years = num // 365
r = num % 365
week  = r // 7
day =  r % 7

print(f"{num} jours ==> {years}annee(s), {week} semaine(s) et {day} jour(s)")
