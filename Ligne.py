#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Produit import Produit


class Ligne(object):
    def Produire(self, aDate : int) -> None:
        pass
    def __init__(self):
        self.___numero : int = None
        self.___produit_en_Cours : Produit = None
        self.___dernier_Produit_fini : Produit = None
        self._listes_commandes = []


