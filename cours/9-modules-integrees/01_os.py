# Module intégré donc import os tout court
import os

# A ne pas faire : chemin absolu
chemin = "D:/python/mon-projet/mon-fichier.py"

# Utiliser les chemins relatifs
chemin = os.path.join(os.getcwd(), "mon-fichier.py")

# Utiliser os.path.join et non concaténation
chemin = os.getcwd() + "\mon-fichier.py"

# Vérifier l'existence d'un fichier
print(os.path.isfile(chemin))

# Changer de répertoire courant
chemin_nouveau_repertoire = os.path.join(os.getcwd(), "data")
# os.mkdir(chemin_nouveau_repertoire)
# os.chdir(chemin_nouveau_repertoire)

os.makedirs("data", exist_ok=True)

print(os.getcwd())

# récupérer nom et extension d'un fichier
nom, extension = os.path.splitext("fichier.py")
print(nom, extension)

# liste les dossiers et fichiers
print(os.listdir(os.getcwd()))