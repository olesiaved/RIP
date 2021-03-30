import random
from Type_produit import Type_produit
from Production import Production
from Box_manager import Box_manager
import os

#initialisation adresse dossier donnée
dir = os.path.dirname(__file__)
filename = os.path.join(dir, './InstanceE.txt')

#creation entité production et run de simulation_production
pr=Production()
pr.simulation_production(filename)


