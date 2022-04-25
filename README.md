# Metro-Boulot-Dodo
Projet Algorithmique de Graphes 2022

Rapport Projet Algorithmie des Graphes

Notre projet est découper en plusieurs fichiers :

data.txt :

    Ajout des lignes ‘L’. Chaque ligne stock les stations d’une ligne du métro parisien de la sorte :
    « L numéro_ligne numéro_des_stations » trouvé grâce à un algorithme.

    Ajout des lignes ‘T’. Chaque ligne stock les stations terminus d’une ligne du métro parisien de la sorte :
    « T numéro_ligne numéro_des_stations ». (Cette opération a été faites à la main)

parse.py :

    Ouvre le fichier data et effectue les opération en fonction de la première lettre de chaque ligne.
    On transforme chaque ligne en liste puis on rentre ses informations dans différents dictionnaires.

graph.py :

    Contient les classes Line(), Vertex() et Graph().

    Line() crée les lignes du métro et leur attribut le nom des lignes, les stations de la ligne ainsi que les stations  terminus de la ligne.

    Vertex() crée les sommets du graphe (les stations) avec leur id, leur nom et les voisins de ceux-ci

    Graph() introduit la notion d'arête pour chaque sommet  et Dijkstra (on va s’attarder sur celui ci) :

    dijkstra(self, start_vertex) prend en argument un sommet de départ et il vérifie si ce sommet existe. Puis, regarde tous les sommets voisins afin de vérifier si ils ont été visité (pour l’instant il n’y en a aucun de visité, donc il stock l’intégralité des voisins dans une liste).
    On visite ensuite chacun des voisins dans le graphe, en rajoutant les nouveaux voisins à la liste, et en sauvegardant le chemin au coût le plus faible dans une nouvelle variable variable.
    Quand tous les chemin ont été visité, la liste des sommets voisins est vide donc on arrête Dijkstra et on renvoie le coût minimum et le chemin associé.

    Concernant l'affichage, les fonctions implémentées ne vérifient pas si la la ligne de métro possède plusieurs terminus, pour cela il aurait fallu différencié plusieurs chemins dans une même ligne de métro, par exemple pour la ligne 7, on se retrouverait avec 2 lignes différentes, l'une ayant pour terminus [La Courneuve - 8 Mai 1945, Marie d'Ivry] et l'autre [La Courneuve - 8 Mai 1945, Villejuif - Louis Aragon], puis tester si la station recherché est disponible dans l'un des 2 "sous-lignes"

loop.py :

    Possède une fonction pour vérifier si le graphe mis en paramètre est connexe ou non 

utilities.py :

    Contient une fonction permettant de vérifier si les sommet ont déjà été visité et une autre permettant d’afficher les arguments requis afin de lancer le programme

set.py :

    new_vertices_edges() crée des classes Vertex() vide puis ses sommets sont remplis avec un dico obtenu via parse(), pareil pour Line(), par contre terminus est une information qui est stocké dans Line() 

    new_graph() crée le graphe.