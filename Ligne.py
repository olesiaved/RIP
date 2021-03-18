#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit


class Ligne(object):
    def Produire(self, aDate : int) -> None:
        pass
    def __init__(self,n):
        self.___numero=n
        self.___produit_en_Cours : Produit = None
        self.___dernier_Produit_fini : Produit = None
        self._listes_commandes = []

    def affichage(self):
        print ("Ligne", self.___numero)

        for element in self._listes_commandes:
            element.affichage()

