"""
Un programme qui demande à l'utilisateur de saisi r
des noms de chats et le programme se stop une fois que
l'utilisateur décide d'arrêter la saisie et
doit nous retourner la liste des chats saisies dans
l'ordre de saisie
Votre programme doit gérer les exceptions de saisie.
Bonus : ne pas pouvoir saisir deux fois le même nom
et afficher le numéro du chat à saisir
( exemple : saisir chat numéro 1 etc ... )
"""

chats = []
reponse = ""
mots_stop = ["stop", "exit", "quit", "quitter"]

# Gestion de la saisie
while reponse.lower() not in mots_stop:
    reponse = input(f"Entrez un nom de chat n°{len(chats)+1} :")
    reponse = reponse.strip().lower().capitalize()
    # if reponse.lower() in mots_stop:
    #     break
    try:
        if reponse == "":
            raise ValueError("Attention pas de nom vide.")
    except ValueError as error:
        print(error)
    else:
        if reponse.lower() not in mots_stop:
            if reponse not in chats:
                chats.append(reponse)
            else:
                print(f"Vous avez déjà saisi le nom {reponse}.")

# Gestion d'affichage
for index, nom_chat in enumerate(chats):
    print(f"Chat n°{index+1}: {nom_chat}")