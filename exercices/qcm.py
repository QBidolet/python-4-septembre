question_1 = "Quel est le ... ?"
question_2 = "Quel est le ... ?"
question_3 = "Quel est le ... ?"

questions = {
    question_1: "a",
    question_2: "a",
    question_3: "b",
}

ma_liste = ["a", "b"]
saisie = input()
while saisie not in ma_liste:
    saisie = input()
for question in questions:
    print(question)