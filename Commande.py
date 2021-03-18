#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit 

class Commande(object):
    def FinDeProdCommande(self) -> None:
        pass

    def __init__(self, id, stock, dP, p, nb):
        self.___id = id
        self.___stockMin = stock
        self.datePrevue = dP
        self.penalite = p
        self.nbproduits=nb
        self.dateReel =None
        self.___num_ligne : int = None
        self._liste_produits_afaire = []
        self._liste_produits_finis = []
    def affichage(self):
        print ("Commande", self.___id, " ", self.___stockMin, " ", self.___datePrevue, " ", self.___penalite," ", self.___nbproduits)
