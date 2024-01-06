
from fonctions import list_of_files, cleaned, calcule_tf_idf, matrice_vec, inversion_matrice, useless, higher_tf_idf, list_speech
#Consigne : afficher le mot le plus répété chez Chirac
#list_most_repeated_words = higher_tf_idf("Speeches")
#print(list_most_repeated_words[0])
#print(list_most_repeated_words[1])

#Consigne : afficher qui a parlé de la nation et combien de fois
#for file in list_speech:
    #with open("Speeches/"+file.split(".")[0]+"-cleaned.txt", 'r', encoding='utf-8') as f1:
        #content = f1.read()
        #words = content.split()
        #cpt = 0
        #for word in words:
            #if word == "nation":
                #verif = True
                #cpt += 1
        #if verif == True:
            #print("Il y a ",cpt," fois nation dans ", file)

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




