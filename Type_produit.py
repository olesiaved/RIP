#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Type_box import Type_box


class Type_produit(object):
    def __init__(self,id,s, p, h, l, nb):
        self.id = id
        self.s = s
        self.p = p
        self.htype = h
        self.ltype = l
        self.nbEmpileMax = nb
        self.type_box : Type_box = None

    def affichage(self):
        print ("Type_produit", self.id, " ", self.s, " ", self.p, " ", self.htype, " ", self.ltype, " ", self.nbEmpileMax)
    
