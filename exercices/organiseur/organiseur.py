# Vous devez construire un organisateur
# de fichier à partir de ce dictionnaire.
# Le programme scannera un dossier
# dans lequel il y a des fichiers (text, pdf ...)
# et devra créer le dossier correspondant
# au clé du dictionnaire, si durant le scan
# on trouve des fichiers il faudra les déplacer
# dans le dossier correspondant.
# Exemple : dans mon dossier il y a un fichier .pdf,
# le programme doit créer le dossier PDF
# et déplacer le fichier à l'intérieur
import os
import shutil

folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

chemin = os.path.join(os.getcwd(), "A TRIER")
liste_fichier = os.listdir(chemin)
for nom_fichier in liste_fichier:
    _, extension = os.path.splitext(nom_fichier)
    for key, values in folder_dict.items():
        if extension in values:
            chemin_dossier = os.path.join(os.getcwd(), key)
            os.makedirs(chemin_dossier, exist_ok=True)
            chemin_fichier = os.path.join(chemin, nom_fichier)
            shutil.move(chemin_fichier, chemin_dossier)

chemin_a_trier = os.path.join(os.getcwd(), "A TRIER")
for element in os.scandir(chemin_a_trier):
    if element.is_file():
        _, extension = os.path.splitext(element.name)
        # print(extension)
        for key, values in folder_dict.items():
            if extension in values:
                chemin_dossier = os.path.join(os.getcwd(), key)
                os.makedirs(chemin_dossier, exist_ok=True)
                chemin_element = os.path.join(chemin_a_trier, element.name)
                shutil.move(chemin_element, chemin_dossier)


chemin_a_trier = os.path.join(os.getcwd(), "A TRIER")
for folder, subfolders, files in os.walk(chemin_a_trier):
    for file in files:
        _, extension = os.path.splitext(file)
        for key, values in folder_dict.items():
            if extension.lower() in values:
                chemin_dossier = os.path.join(os.getcwd(), key)
                os.makedirs(chemin_dossier, exist_ok=True)
                chemin_element = os.path.join(folder, file)
                shutil.move(chemin_element, chemin_dossier)
