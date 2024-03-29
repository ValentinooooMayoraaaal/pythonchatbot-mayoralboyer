import os
import math
from collections import defaultdict
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
#Fonction des professeurs qui permet de récupérer le nom de chaque fichier d'un module.
#On doit mettre le nom du module et le format du document en variable de cette fonction


#Je crée ensuite une seconde liste qui me sera bien utile. Je l'appelle "new_list_speech"

new_list_speech = []

#Ici je fais la première consigne du TP, je fais réduire le nom de chaque texte de ma première liste, et je vais les surnommé par uniquement la partie intéressante, soit celle de leur nom de famille. "nomination-CHirac1" devient "Chirac1". Et je mets ces nouveaux surnoms dans la nouvelle liste (j'ai essayé de simplement modifié la liste initiale mais je n'avais pas réussi donc j'ai finis par créer une nouvelle liste).
list_speech = list_of_files("Textes", ".txt")

list_speech = list_of_files("Textes", ".txt")
for speech in list_speech:
    speech = speech[11:-4]
    new_list_speech.append(speech)

presidents = {new_list_speech[0]:"Jacques", new_list_speech[1]:"Jacques", new_list_speech[2]:"Valéry", new_list_speech[3]:"François",new_list_speech[4]:"Emmanuel", new_list_speech[5]:"François", new_list_speech[6]: "François", new_list_speech[7]:"Nicolas"}


#Pour la seconde consigne, j'initialise en brut un dictionnaire. J'associe pour chaque textes de la nouvelle liste, le prénom du président qui va avec. Au début j'ai voulu mettre comme clé les prénoms, mais je me retrouvais à avoir deux fois la même clé (notamment pour "Jacques" qui devait être associé à deux textes). Donc j'ai décidé de faire des noms de ma nouvelles listes, les clés auxquelles j'associe les prénoms des présidents, un jolie moyen de gruger le systême. J'ai pas mal duré pour créer ce dictionnaire mais finalement il est bien fonctionnel. Il affiche le nom des textes simplifié et le prénom des présidents associés. Les "print" que j'ai mis partout c'est pour à chaque fois suivre l'évolution de chaque élément au fur et à mesure du code. Si tu veux essayer ce code, tu dois créer ton nouveau projet, aller dans les fichiers de ton ordinateur, puis dans "pycharmproject" et dans ce nouveau projet tu mets les fichiers textes qui sont sur moodle. Ca te les fera directement apparaître sur ton nouveau projet pycharm. Et tu les mets dans un module intitulé "Textes".

presidents = {new_list_speech[0]:"Jacques", new_list_speech[1]:"Jacques", new_list_speech[2]:"Valéry", new_list_speech[3]:"François",new_list_speech[4]:"Emmanuel" , new_list_speech[5]:"François", new_list_speech[6]: "François", new_list_speech[7]:"Nicolas"}


noms = []

for speech in new_list_speech:
    for char in speech:
        if 47 < ord(char) < 58 :
            speech = speech[:-1]
    if speech not in noms:
        noms.append(speech)

def cleaned(src_dir, cleaned_dir):
    filenames = list_of_files(src_dir, "txt")
    for file in filenames:
        open_path = src_dir + "/" + file
        cleaned_path = cleaned_dir + "/" + file.split(".")[0] + "-cleaned.txt"
        with open(open_path,"r",encoding="utf-8") as f, open(cleaned_path, "w", encoding="utf-8") as f2:
            content = f.readlines()
            for line in content:
                cleaned_content = ""
                for c in line:
                    if 65 <= ord(c) <= 90:
                        c = chr(ord(c) + 32)
                    if not (97 <= ord(c) <= 122 or c == "é" or c == "É" or c == "ç" or c == "à" or c == " " or c == "'" or c=="," or c=="ô" or c=="ù" or c=="."):
                        c = ""
                    if c == "'" or c =="," or c ==".":
                        c = " "
                    cleaned_content += c
                f2.write(cleaned_content)
cleaned("Textes", "Speeches")

def counting_words(directory):
    word_occurrences = defaultdict(int)

    for filename in os.listdir(directory):
        if filename.endswith("-cleaned.txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                words = content.split()
                for word in words:
                    word_occurrences[word] += 1
    print(word_occurrences)
    return dict(word_occurrences)
directory= "./Speeches"

def calcule_tf_idf(file_path):
    tf_idf_scores = defaultdict(float)
    numbr_of_docu_having_this_word = defaultdict(float)
    total_documents = len(presidents.keys())

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    unique_words = set(content.split())

    for word in unique_words:
        numbr_of_docu_having_this_word[word] += 1
    word_count = defaultdict(int)

    with open(file_path, "r", encoding="utf-8") as f:
        for word in f.read().split():
            word_count[word] += 1

    for word, count in word_count.items():
        tf_idf_scores[word] += ((count / len(unique_words)) * (math.log10(total_documents / (numbr_of_docu_having_this_word[word] + 1))))
    return dict(tf_idf_scores)

    return dict(tf_idf_scores)

def matrice_vec(src_dir):
    mat = []
    for i in range(len(list_speech)):
        liste = []
        for files in list_speech:
            f1 = calcule_tf_idf(src_dir + "/" + files.split(".")[0]+"-cleaned.txt")
            for j in range(len(f1)):
                liste[j]= liste.append(f1.values())
            mat.append(liste)
        return mat
    #On crée une matrice avec dans chaque ligne tous les vecteurs de chaque mots à l'intérieur
#Maintenant on transforme les lignes et colonnes et les colonnes en ligne.


def inversion_matrice(mat):
    inv_mat = []

    for j in range(len(mat[0])):
        new_row = []


        for i in range(len(mat)):

            new_row.append(mat[i][j])


        inv_mat.append(new_row)

    return inv_mat
matrice = inversion_matrice(matrice_vec("Speeches"))
def useless(src_dir): #Je prends comme paramètre le fichier contenant mes documents contenant mes mots
    mots_inutiles = [] #j'initialise une liste vide de mots inutiles
    for file in list_speech: #Pour chaque document dans mon fichier choisi comme paramètre, j'éxecute la suite
        transi = {} #Je crée un dictionnaire de transition
        file_path = src_dir + "/" + file.split(".")[0] + "-cleaned.txt" #Je recontruis le nom des documents que je cherche et j'ajoute la mention "-cleaned.txt" qu'ils auront forcément puisqu'ils ont été nettoyés avant
        transi =calcule_tf_idf(file_path) #J'ajoute au dictionnaire de transition, le dictionnaires de valeurs TFIDF du document
        for key in transi.keys(): #Pour chaque clé dans les clés du dictionnaire de mot
            if transi[key] == 0: #Je regarde si la valeur associée à cette clé = 0
                mots_inutiles.append(transi.keys()) #Si c'est le cas, je l'ajoute à ma liste mot inutile
    return mots_inutiles

def higher_tf_idf(src_dir):
    All_goat_of_each_file_in_a_folder = [] #J'initialise la liste qui contiendrait les mots de chaque fichier qui aura le tfidf le plus élevé
    for file in list_speech: #Classique, je réutilise le nombre de fichier de ma variable list_speech
        file_path = src_dir + "/" + file.split(".")[0] + "-cleaned.txt" #Je recrée leur nom qui se terminera forcément pas "-cleaned.txt" car on cherchera toujours à utiliser les fichiers nettoyer
        dico_tf_idf_of_file_path = calcule_tf_idf(file_path) #Je mets le dico du fichier, actuellemennt dans la boucle, dans une nouvelle variable pour que ce soit plus clair
        max = 0 #Je vais dire que 0 de ce dictionnaire est le maximum
        for key in dico_tf_idf_of_file_path.keys(): #Puis je fais une boucle pour trouver le véritable maximum des tf-idf du dictionnaire en parcourant chaque clé du dico
            if dico_tf_idf_of_file_path[key] > max: #Si la valeur associé à la clé est supérieur au maximum, la valeur devient le maximum et key_max conserve le mot associé à cette valeur maximum
                max = dico_tf_idf_of_file_path[key]
                key_max = key
        All_goat_of_each_file_in_a_folder.append(key_max) #J'ajoute le mot à la liste des goats de chaque fichier du dossier
    return All_goat_of_each_file_in_a_folder

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

