#Fonction des professeurs qui permet de récupérer le nom de chaque fichier d'un module. 
#On doit mettre le nom du module et le format du document en variable de cette fonction

import os
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

def cleaned(file):
    with open(file,"r",encoding="utf-8")as f:
        speech = []
        for lines in f:
            cleaned_content = ""
            for c in lines:
                if 65 <= ord(c) <= 90:
                    c = chr(ord(c) + 32)
                if not (97 <= ord(c) <= 122 or c == "é" or c == "É"):
                    c = ""
                cleaned_content += c
            speech.append(cleaned_content)
        return speech




for i in range(len(list_speech)):
    with open(f"Speeches/min_list_speech_{i}.txt", "w", encoding="utf-8") as f1, open(f"Textes/{list_speech[i]}", "r", encoding="utf-8") as f2:
        f1 = cleaned(f"Textes/{list_speech[i]}")