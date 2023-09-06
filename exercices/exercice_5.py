"""
A partir de cette liste
["Jean", "Maximilien", "Brigitte", "Sonia"]
Coder un programme permettant de séparer
les prénoms, c'est-à-dire une liste avec ceux
ayant moins de 6 caractères (6 inclus)
et ceux ayant plus de 6 caractères.
"""

# prenoms = ["Jean", "Maximilien", "Brigitte", "Sonia"]
# prenoms_inf_6 = []
# prenoms_sup_6 = []
#
# for prenom in prenoms:
#     if len(prenom) > 6:
#         prenoms_sup_6.append(prenom)
#     else:
#         prenoms_inf_6.append(prenom)
#
# print(prenoms_sup_6)
# print(prenoms_inf_6)

prenoms = ["Jean", "Maximilien", "Brigitte", "Sonia"]

prenoms_sup_6 = [element for element in prenoms if len(element) > 6]
prenoms_inf_6 = [element for element in prenoms if len(element) <= 6]

# liste avec les 10 premiers nombres pairs au carré
liste = [element ** 2 for element in range(0, 20) if element % 2 == 0]
print(liste)
