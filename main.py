import random
from Type_produit import Type_produit
from Production import Production
from Box_manager import Box_manager
import os
dir = os.path.dirname(__file__)
filename = os.path.join(dir, './Donnee1.txt')
pr=Production()
pr.simulation_production(filename)
p0=0
p1=0
p2=0
p3=0
p4=0
p=[0,0,0,0,0]
for i in pr._schedule._liste_lignes:
    for j in i._listes_commandes:
        j.affichage()
print(p)
print(p0,p1,p2,p3,p4)

print(pr._schedule.box_manager._listes_box)
