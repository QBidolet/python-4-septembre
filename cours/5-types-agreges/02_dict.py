mon_dict = {
    "nom": "BIDOLET",
    "prenom": "Quentin"
}

print(mon_dict["prenom"])

# parcours d'un dict
for element in mon_dict.keys():
    print(element)

print("#"*25)
for value in mon_dict.values():
    print(value)

print("#"*25)
for key, value in mon_dict.items():
    print(key, value)

# Exemple

users = {
    "125A": {
        "nom": "BIDOLET",
        "prenom": "Quentin",
        "age": 29,
        "competences": ["Python"]
    },
    "125B": {
        "nom": "DUPONT",
        "prenom": "Jean",
        "age": 92,
        "competences": ["Cobol"]
    },
}
