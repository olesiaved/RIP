import random
from Type_produit import Type_produit
from Production import Production
from Box_manager import Box_manager
import os


# Afin d'implementer notre solution partielle il est nécessaire de run notre classe Main

# Dans cette classe Main le nom du fichier txt contenant les données y est précisé
# (ainsi le programme peut facilement être utilisé peu importe le nom du fichier txt)

# Dans le main une entitée Production est créée et sa fonction simulation_production est appelée afin de traiter les données
# créer et remplir le fichier solution (résolution de l'ensemble du problème informatique)








#initialisation adresse dossier donnée
dir = os.path.dirname(__file__)
filename = os.path.join(dir, './Donnee1.txt')

#creation entité production et run de simulation_production
pr=Production()
pr.simulation_production(filename)


