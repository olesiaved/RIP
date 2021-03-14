#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit 

class Commande(object):
    def FinDeProdCommande(self) -> None:
        pass

    def __init__(self):
        self.___id = None
        self.___stockMin = None
        self.___datePrevue = None
        self.___penalite = None
        self.___dateReel = None
        self.___num_ligne : int = None
        self._liste_produits_afaire = []
        self._liste_produits_finis = []

