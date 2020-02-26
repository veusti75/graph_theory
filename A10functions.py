import numpy as np
from numpy import linalg as LA
def chargement_graphe(nom_du_fichier):
    graphe = open(nom_du_fichier)

    global sommets,a,b  # rend utilisable la variable pour toutes les fonctions
    sommets = graphe.readline()
    sommets = int(sommets)
    matrice_arcs=[]
    for i in range(sommets+1):
        matrice_arcs.append([0] * (sommets+1))
    

    arcs = graphe.readline()
    arcs = int(arcs)
    matrice_poids=[]

    for i in range(sommets+1):
        matrice_poids.append(["*"] * (sommets+1))

    for i in range(arcs):
        connexion = graphe.readline()
        a, b = connexion.split(",")
        b,c = b.split(" ")
        a = int(a)
        b = int(b)
        c = int(c)
        matrice_arcs[a][b]=1
        matrice_poids[a][b]=c

    graphe.close()

    return matrice_arcs,matrice_poids



def affichage_adj(A):
    arcs= np.array(A)
    print(arcs)
    
def affichage_poids(P):
    poids= np.array(P)
    print(poids)
    

def detection_circuit(A): # Méthode 1 présent ou non sur la diagonale de la fermeture transitive     
    s=0
    for i in range(1,sommets):
        matrice_transitive=LA.matrix_power(A,i)
        s=s+matrice_transitive
    #print(s)

    if sum(np.diag(s))!=0:
            print("Circuit présent")
    else:
            print("Pas de circuit")
            
"""
Pour calculer le rang de chaque sommet quand il n'y a pas de circuit, il aurait fallu désigner le sommet qui n'a pas de prédécesseur commme racine
, puis tant que le parcours n'est pas terminé, supprimer la racine et réitérer l'opération jusqu'à la fin. Le nombre de fois où la boucle aurait été exécutée
correspondrait au rang du sommet en question.
"""
