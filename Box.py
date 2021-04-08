#!/usr/bin/python
# -*- coding: UTF-8 -*-

#entité box (basé sur un type de box) attribuée à 1 seul produit pour la solution triviale
class Box(object):

    #prochainement utile
    def ViderBox(self):
        self._id_commande=None
        self._produit=[]
        self._type_pile=[]



    def __init__(self, n, type):
        self._numero=n
        self._produit  = [] #produit attribué à cette box
        self._type_pile=[]
        self._type=type
        self._id_commande=None
        """# @AssociationMultiplicity 1"""
    def affichage(self):
        print(self._numero," ", " ", self._id_commande)
        self._type.affichage()
