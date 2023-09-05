# Définition d'une fonction
def do_nothing():
    pass


def somme(a, b):
    return a + b


resultat = somme(1, 2)
print(resultat)


# *args
def print_2(*args, end="\n"):
    for arg in args:
        print(arg, end=end)


# print_2("Hello", "World!", end=" ")

# Retour multiple
def items():
    return "Item 1", "Item 2"


item_1, item_2 = items()
print(item_1, item_2)


# **kwargs
def menu(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        dict.update({key: value})
    return dict


resultat = menu(vin="Bourgogne", entree="entree",
                plat="plat", dessert="dessert")
print(resultat)

# fonction anonyme
print("#" * 25)
liste = [1, 2, 3, 4]


def double(a):
    return a * 2


# for nombre in liste:
#     print(double(nombre))
mon_map = map(double, liste)
print(list(mon_map))

mon_map = map(lambda x: x * 2, liste)
print(list(mon_map))

# filter
ma_liste = [6, 7, 8, 9]
nombre_pair_filter_object = filter(lambda x: x % 2 == 0, liste)
nombres_pairs = list(nombre_pair_filter_object)
print(nombres_pairs)

# closure
def fonction_externe():
    compteur = 10
    def fonction_interne():
        return 5 + compteur
    return fonction_interne

ma_fonction = fonction_externe()
print(ma_fonction())


# fonction génératrice
def range_2(n):
    compteur = 0
    while compteur < n:
        yield compteur
        compteur += 1


for i in range_2(5):
    print(i)