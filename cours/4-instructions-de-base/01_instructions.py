nom = "BIDOLET"
prenom = "Quentin"

# condition
if nom == "Julien":
    print("Hello")
elif prenom == "Michel":
    print("Michel")
else:
    print("Aucune des conditions n'a été rempli.")

# boucle for
for caractere in nom:
    print(caractere, end="")

print("#"*25)

# enumerate
for indice, caractere in enumerate(nom):
    print(indice, caractere, sep="-", end="\n\n")

# range
for i in range(6):
    print(i)

# while
i = 0
while i < 6:
    print(i)
    i += 1