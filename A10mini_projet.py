from A10affichage_fichier import display_file
from A10functions import chargement_graphe
from A10functions import affichage_adj
from A10functions import affichage_poids
from A10functions import detection_circuit


nom_du_fichier = input("Veuillez insérer le nom du fichier ")

while nom_du_fichier !="aucun":


	A, P = chargement_graphe(nom_du_fichier)

	display_file(nom_du_fichier)

	print("Matrice d_adjacence du",nom_du_fichier)
	affichage_adj(A)

	print("Valeurs des arcs")
	affichage_poids(P)

	detection_circuit(A)
	nom_du_fichier = input("Veuillez insérer le nom du fichier ")






