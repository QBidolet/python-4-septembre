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