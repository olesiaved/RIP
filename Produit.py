#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Type_produit import Type_produit
from Type_box import Type_box

#classe entité produit (basée sur la classe type produit)
class Produit(object):

    def __init__(self,id_commande,Type_produit):
        self._dateDebutProd : int = None     # date début de prod du produit
        self._dateFinProd : int = None       # date fin de prod du produit
        self._id_commande = id_commande      # id commande à laquelle le produit est rattaché
        self._box=None         # numero de la box attribuée au produit
        self._type = Type_produit            # type de produit
        """# @AssociationMultiplicity 1"""

    def affichage(self):
        print(self._type.id," ", self._dateDebutProd, " ", self._dateFinProd)
        self._box.affichage()

