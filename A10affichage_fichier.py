import numpy as np

def display_file(nom_du_fichier):

	graphe = open(nom_du_fichier)



	    
	sommets = graphe.readline()
	arcs = graphe.readline()
	reste = graphe.read() ## lit les lignes restantes

	reste = reste.replace(' ','=')
	reste = reste.replace(',','->')

	sommets = int(sommets) ## Cast: Passe de type String au type int
	arcs = int(arcs)





	graphe.close()  ## Ferme le fichier .txt l'empêchant ainsi d'être modifié


	print("* Lecture du graphe sur fichier")
	print(sommets,"sommets")
	print(arcs,"arcs")
	print(reste)
	print(" ")
