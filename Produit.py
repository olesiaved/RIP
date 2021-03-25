#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Type_produit import Type_produit
from Type_box import Type_box

class Produit(object):
    def SetDateDebutProd(self, aDateDebutProd : int) -> None:
        pass

    def __init__(self,id_commande,Type_produit):
        self._dateDebutProd : int = None
        self._dateFinProd : int = None
        self._id_commande = id_commande
        self._num_box : int = None
        self._type = Type_produit
        """# @AssociationMultiplicity 1"""

    def affichage(self):
        print(self._type.id," ", self._dateDebutProd, " ", self._dateFinProd, " ", self._num_box)

