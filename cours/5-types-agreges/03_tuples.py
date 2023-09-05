# Un tuple est une liste immuable.

# Un tuple vide.
mon_tuple = ()
print(type(mon_tuple))

mon_tuple = (99, 22)
print(mon_tuple)

mon_tuple = 99, 22
# print(type(mon_tuple))
# mon_tuple = 99,
# mon_tuple = (99,)

# unpacking
a, b = mon_tuple
print(a, b)

# syntaxe retour d'une fonction
def ma_func():
    return 10, 99

a, b = ma_func()
print(a, b)

resultat = ma_func()
print(type(resultat))

print("#"*25)
for element in resultat:
    print(element)
print(resultat[1])

# Immuable, sans modification ni suppression.
# del resultat[0]
# print(resultat)