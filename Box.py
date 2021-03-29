#!/usr/bin/python
# -*- coding: UTF-8 -*-




# Afin d'implementer notre solution partielle il est nécessaire de run notre classe Main

# Dans cette classe Main le nom du fichier txt contenant les données y est précisé
# (ainsi le programme peut facilement être utilisé peu importe le nom du fichier txt)

# Dans le main une entitée Production est créée et sa fonction simulation_production est appelée afin de traiter les données
# créer et remplir le fichier solution (résolution de l'ensemble du problème informatique)





#entité box (basé sur un type de box) attribuée à 1 seul produit pour la solution triviale
class Box(object):
    #prochainement utile
    def ViderBox(self):
        pass


    def __init__(self, n, type):
        self.___numero=n
        self._produit  = None #produit attribué à cette box
        self._type=type
        """# @AssociationMultiplicity 1"""

