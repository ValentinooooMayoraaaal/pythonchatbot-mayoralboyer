
from fonctions import list_of_files, cleaned, calcule_tf_idf, matrice_vec, inversion_matrice, useless, higher_tf_idf, list_speech
#Consigne : afficher le mot le plus répété chez Chirac
def higher_Chirac():
    list_most_repeated_words = higher_tf_idf("Speeches")
    return(list_most_repeated_words[0],list_most_repeated_words[1])


#Consigne : afficher qui a parlé de la nation et combien de fois
def nation_repetition():
    for file in list_speech:
        with open("Speeches/"+file.split(".")[0]+"-cleaned.txt", 'r', encoding='utf-8') as f1:
            content = f1.read()
            words = content.split()
            cpt = 0
            for word in words:
                if word == "nation":
                    verif = True
                    cpt += 1
            if verif == True:
                print("Il y a ",cpt," fois nation dans ", file)

#Consigne : Indiquer le premier président à parler du climat et/ou de l’écologie
def Qui_parlait_écologie():
    list_écolo = []
    list_climato = []
    list_chronologique = ["Giscard dEstaing", "Mitterrand", "Chirac", "Sarkozy", "Hollande", "Macron"]
    for file in list_speech:
        dico = calcule_tf_idf("Speeches/" + file.split(".")[0] + "-cleaned.txt")
        for key in dico.keys():
            if key in ("climat", "climatique"):
                list_climato.append(file[11:-4])
            if key in ("écologie", "écologique"):
                list_écolo.append(file[11:-4])
    cpt_écolo = 0
    cpt_climato = 0
    for president in list_chronologique:
        if (president in list_climato) and cpt_climato != 1:
            print(president, "est le premier président à avoir aborder la thématique du climat.")
            cpt_climato = 1
        if (president in list_écolo) and cpt_écolo != 1:
            print(president, "est le premier président à avoir aborder la thématique de l'écologie.")
            cpt_écolo = 1

def mots_repetes_par_tous():
    mots_repaire = []
    for word in calcule_tf_idf("Speeches/Nomination_Chirac1-cleaned.txt").keys():
        mots_repaire.append(word) #je mets tous les mots du premier doc dans une liste
        for file in list_speech[1:]:  #Je vais utiliser tous les documents sauf le premier qui me sert de comparaison
            for i in range(len(mots_repaire)-1): #Pour tous les mots dans la liste mots_repaire
                if mots_repaire[i] not in calcule_tf_idf("Speeches/"+file.split(".")[0]+"-cleaned.txt").keys(): #S'il n'y a pas le mot de la liste repaire dans le mots du nouveau document
                    mots_repaire.remove(mots_repaire[i]) #Alors on retire de la liste mots_repaire, le terme qui n'est pas dans les mots dees autres documents
    mots_importants = []
    for i in range(len(mots_repaire)-1):
        if len(mots_repaire[i])>4:
            mots_importants.append(mots_repaire[i])
    return mots_importants

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



