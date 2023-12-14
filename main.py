#Fonction des professeurs qui permet de récupérer le nom de chaque fichier d'un module. 
#On doit mettre le nom du module et le format du document en variable de cette fonction

import os
import math
from collections import defaultdict
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

#Dans mon pycharm j'ai mis tous les fichiers .txt dans un module nommé "Textes" donc je le précise ici(il faudra juste créer ce même module dans github avec les mêmes textes mais je ne sais pas faire pour l'instant). Ca crée donc une liste dans laquelle chaque valeur sera le nom de chaque textes. Je donne à cette liste le nom de "list_speech".

list_speech = list_of_files("Textes", ".txt")

#Je crée ensuite une seconde liste qui me sera bien utile. Je l'appelle "new_list_speech"

new_list_speech = []

#Ici je fais la première consigne du TP, je fais réduire le nom de chaque texte de ma première liste, et je vais les surnommé par uniquement la partie intéressante, soit celle de leur nom de famille. "nomination-CHirac1" devient "Chirac1". Et je mets ces nouveaux surnoms dans la nouvelle liste (j'ai essayé de simplement modifié la liste initiale mais je n'avais pas réussi donc j'ai finis par créer une nouvelle liste).

for speech in list_speech:
    speech = speech[11:-4]
    new_list_speech.append(speech)

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
                    if not (97 <= ord(c) <= 122 or c == "é" or c == "É" or c == "ç" or c == "à" or c == " " or c == "-" or c == "'"):
                        c = ""
                    if c == "-" or c == "'":
                        c = " "
                    cleaned_content += c
                f2.write(cleaned_content)

cleaned("Textes", "Speeches")

def calcule_tf_idf(file_path):
    tf_idf_scores = defaultdict(float)
    idf_scores = defaultdict(float)
    total_documents = 0

    for key in presidents.keys():
        total_documents += 1

        with open(file_path, "r", encoding="utf-8") as f:
            # Ceci fait une liste des mots uniques du document en question grâce à la fonction set()
            unique_words = set(f.read().split())

        for word in unique_words:
            idf_scores[word] += 1

        word_count = defaultdict(int)

        with open(file_path, "r", encoding="utf-8") as f:
            # On revient au début du fichier pour le lire à nouveau
            for word in f.read().split():
                word_count[word] += 1

        for word, count in word_count.items():
            tf_idf_scores[word] += ((count / len(unique_words)) * (math.log(total_documents / (idf_scores[word])+1)))

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
print(matrice)

