import os
import shutil

# copier des fichiers et dossiers
# on peut aussi renommer dans le nom de destination
# attention si fichier existant, il sera écrasé

src = os.path.join(os.getcwd(), "test.txt")
dst = os.path.join(os.getcwd(), "data", "test_2.txt")
shutil.copy(src, dst)

# copie récursive
src = os.path.join(os.getcwd(), "data")
dst = os.path.join(os.getcwd(), "data_backup")
shutil.copytree(src, dst)

# suppression récursive
shutil.rmtree("data_backup")

# déplacement
src = os.path.join(os.getcwd(), "test.txt")
dst = os.path.join(os.getcwd(), "data")
shutil.move(src, dst)
