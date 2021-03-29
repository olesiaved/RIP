import random
from Type_produit import Type_produit
from Production import Production
from Box_manager import Box_manager
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, './Donnee1.txt')
pr=Production()
pr.simulation_production(filename)


