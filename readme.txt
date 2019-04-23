Hierarchie par defaut

- generate.py       # code generant le site dans un dossier build
- requirements.txt  # list dependances necessaires pour executer generate.py
- infos.txt         # titre site, mail
- cv.txt            # texte cv (affiche dans la page d'accueil)
+ templates  # templates de code html qui seront remplies avec les infos issues
             # des fichiers tels que infos.txt, cv.txt, details.txt...
  - index.html    # template page d'accueil du site
  - project.html  # template page d'un projet
+ projects  # dossier contenant tous les dossiers projets
  + "nom projet"
    + img          # dossier contenant les images du projet
    - icon.png     # image affichee dans index.html
    - details.txt  # texte commentaire du projet (affiche dans la page du projet)


## Installation et Fonctionnement
Le programme est l'ensemble des fichiers décrits ci-dessus. Il
suffit de les copier tels quels dans un dossier vide.

Dans la suite, on referera au chemin dudit dossier par <program_path>
(le vrai chemin doit ressembler a C:\Users\coincoin\monsite)

Le programme permet de generer un site pret a l'emploi, consistant en un
ensemble de fichiers html, css et d'images. 

Par defaut, les fichiers du site genere sont stockes dans le dossier
<program_path>\build.


## Python
Les installeurs Python sont disponibles sur https://www.python.org/downloads/

* installer Python3, version >= 3.6 (par defaut, prendre la dernier version
    disponible). Suivre la procedure d'installation. Cela devrait installer, entre
    autres, un executable du genre C:\"Program Files"\Python3.6\python.exe. On
    referera a ce chemin par <python_exe_path>.

On va maintenant installer un "environnement virtuel Python". Cela permet d'avoir un
python.exe dedie a notre projet, qui accede aux dependances necessaires, listees
dans le fichier requirements.txt.

Dans une console, executer les commandes suivantes (l'une apres l'autre, en
remplacant les references <...> par le vrai chemin) :
* cd <program_path>
* <python_exe_path> -m venv venv
* venv\Scripts\activate
* pip install -r requirements.txt
* deactivate

L'environnement virtuel est installe dans <program_path>\venv. On l'active en
executant venv\Scripts\activate dans une console. Une fois active, la commande
python va renvoyer au python.exe de l'environnement virtuel. On desactive
l'environnement en executant la commande deactivate.


## Generer le site
Pour generer le site, il faut activer l'environnement virtuel, puis executer le
code de generate.py. Dans une console, executer :
* cd <program_path>
* venv\Scripts\activate
* python generate.py
* deactivate


## Conseils pour modifier le site
Generer le site et modifier les fichiers dans le dossier build, pour voir
directement les effets en ouvrant par exemple build\index.html dans un
navigateur. Un fois des modifications satisfaisantes apportées, les reporter sur
les fichiers du programme pour que la prochaine generation du site en tienne
compte.

Le fichier style.css contient les informations de couleurs, tailles, ...
affectant l'esthetique globale du site. Renommer ou supprimer momentanement le fichier pour
voir l'effet de son absence.

Pour plus d'infos sur html/css, on peut consulter https://www.w3schools.com/


## Fichiers de contenu

infos.txt : titre et mail, a specifier commet suit:
title: le titre du site
mail: un@ma.il

cv.txt, details.txt : le contenu de ces fichiers est copie tel quel dans
index.html et le project.html associe respectivement. Pour le moment, il faut
donc ecrire du html directement.

C'est le generate.py qui remplit les templates en remplacant des jetons,
par ex. {{ title }}, par la valeur qu'il a lue dans l'un des fichiers
precedents. Pour ajouter de nouvelles valeurs, il faut adapter le code de
generate.py et des templates.
