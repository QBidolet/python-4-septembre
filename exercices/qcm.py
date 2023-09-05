question_1 = "Q1. Quel est le résultat du calcul 2*2**2 ?\n" \
             "(a)4\n" \
             "(b)5\n" \
             "(c)8\n" \
             "(d)12"

question_2 = "Q2. Quel est le résultat du calcul 2*2**2 ?\n" \
             "(a)4\n" \
             "(b)5\n" \
             "(c)8\n" \
             "(d)12"
question_3 = "Q3. Un set peut il contenir une valeur dupliquée ?" \
             "(a)Oui\n" \
             "(b)Non\n" \
             "(c)Peut être"

questions = {
    question_1: "c",
    question_2: "c",
    question_3: "b",
}

print(" *** Bienvenue sur ce QCM. ***\n\n")
score = 0
for question, reponse in questions.items():
    print(question + '\n')
    reponse_utilisateur = input("Tapez votre réponse (a/b/c/d)")
    if reponse_utilisateur == reponse:
        score += 1
        print("Bonne réponse.")
    else:
        print("Mauvaise réponse.")

# print("Votre score : " + str(score) + "/" + str(len(questions)))
print(f"Votre score : {score}/{len(questions)}.")