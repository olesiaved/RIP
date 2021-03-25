#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit 

class Commande(object):
    def FinDeProdCommande(self) -> None:
        pass

    def __init__(self, id, stock, dP, p,list_prod):
        self._id = id
        self._stockMin = stock
        self._datePrevue = dP
        self._penalite = p
        self._dateReel =None
        self._list_prod = list_prod
        self._num_ligne : int = None
        self._liste_produits_afaire = []
        self._liste_produits_finis = []



    def affichage(self):
        print ("Commande", self._id, " ", self._stockMin, " ", self._datePrevue, " ", self._dateReel, "",self._penalite," ",self._list_prod)

    def DateEnvoieFin(self):
        print(self._stockMin)
        self._dateReel = self._liste_produits_finis[len(self._liste_produits_finis)-1]._dateFinProd + self._stockMin