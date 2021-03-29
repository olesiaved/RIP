#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Type_produit import Type_produit
from Type_box import Type_box



# Afin d'implementer notre solution partielle il est nécessaire de run notre classe "Main"

# Dans cette classe Main le nom du fichier txt contenant les données y est précisé
# (ainsi le programme peut facilement être utilisé peu importe le nom du fichier txt)

# Dans le "Main" une entité "Production" est créée et sa fonction simulation_production est appelée afin de traiter les données
# créer et remplir le fichier solution (résolution de l'ensemble du problème informatique)






#classe entité produit (basée sur la classe type produit)
class Produit(object):

    def __init__(self,id_commande,Type_produit):
        self._dateDebutProd : int = None     # date début de prod du produit
        self._dateFinProd : int = None       # date fin de prod du produit
        self._id_commande = id_commande      # id commande à laquelle le produit est rattaché
        self._num_box : int = None           # numero de la box attribuée au produit
        self._type = Type_produit            # type de produit
        """# @AssociationMultiplicity 1"""

    def affichage(self):
        print(self._type.id," ", self._dateDebutProd, " ", self._dateFinProd, " ", self._num_box)

