#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit 

class Commande(object):
    def FinDeProdCommande(self) -> None:
        pass

    def __init__(self, id, stock, dP, p,list_prod):
        self._id = id
        self.___stockMin = stock
        self._datePrevue = dP
        self._penalite = p
        self._dateReel =None
        self._list_prod = list_prod
        self.___num_ligne : int = None
        self._liste_produits_afaire = []
        self._liste_produits_finis = []



    def affichage(self):
        print ("Commande", self._id, " ", self.___stockMin, " ", self.___datePrevue, " ", self.___penalite," ",self._list_prod)

