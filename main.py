
from fonctions import list_of_files, cleaned, calcule_tf_idf, matrice_vec, inversion_matrice, useless, higher_tf_idf, list_speech, higher_Chirac, nation_repetition, Qui_parlait_écologie, mots_repetes_par_tous

def menu():
    print("Bienvenue dans le menu.")
    print("Ce programme vous permet de recueillir des informations à partir des différents textes de nominations des présidents. En fonction de vos envies, sélectionnez le numéro de votre choix.")
    print("Tapez 1 pour connaître la liste des mots les moins importants dans le corpus de documents.")
    print("Tapez 2 pour connaître les mots les plus répétés pour chacun des discours.")
    print("Tapez 3 pour connaître le mot le plus répété par Jacques Chirac.")
    print("Tapez 4 pour connaître le(s) nom(s) du (des) président(s) qui a (ont) parlé de la « Nation » et celui qui l’a répété le plus de fois.")
    print("Tapez 5 pour connaître le premier président à parler du climat et de l’écologie dans ses discours.")
    print("Tapez 6 pour connaître quels sont les mots importants que tous les présidents ont évoqués.")
    x = int(input("A quel connaissance souhaitez-vous accéder ?"))
    if x == 1: print(useless("Speeches"))
    if x == 2 : print(higher_tf_idf("Speeches"))
    if x == 3 : print(higher_Chirac())
    if x == 4 : print(nation_repetition())
    if x == 5 : print(Qui_parlait_écologie())
    if x == 6 : print(mots_repetes_par_tous())

menu()



