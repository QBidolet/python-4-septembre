# # lever une exception
# nombre = input("Veuillez rentrer un entier.")
# # nombre = int(nombre)
# # print(nombre)
#
# # gérer ce cas particulier
# try:
#     nombre = int(nombre)
# except ValueError:
#     print("Vous n'avez pas rentré un nombre valide.")
# else:
#     print(nombre)
# finally:
#     print("Finally")

# Gérer plusieurs exceptions
try:
    numerateur = float(input("Veuillez rentrer un numerateur."))
    denominateur = float(input("Veuillez rentrer un denominateur."))
    resultat = numerateur/denominateur
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print(resultat)