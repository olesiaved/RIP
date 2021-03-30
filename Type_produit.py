# !/usr/bin/python
# -*- coding: UTF-8 -*-
from Type_box import Type_box

#type de produit et caractéristiques

class Type_produit(object):
    def __init__(self, id, s, p, h, l, nb):
        self.id = id    #id du produit
        self.s = s      #temps de set-up
        self.p = p      #temps de production
        self.htype = h  #hauteur d'un produit
        self.ltype = l  #longueur d'un produit
        self.nbEmpileMax = nb # nombre max sur une pile
        self.type_box: Type_box = None  # type de box "attribué" au produit

    def affichage(self):
        print("Type_produit", self.id, " ", self.s, " ", self.p, " ", self.htype, " ", self.ltype, " ",
              self.nbEmpileMax)
