#!/usr/bin/python
# -*- coding: UTF-8 -*-

#entité box (basé sur un type de box) attribuée à 1 seul produit pour la solution triviale
class Box(object):

    #prochainement utile
    def ViderBox(self):
        pass


    def __init__(self, n, type):
        self.___numero=n
        self._produit  = None #produit attribué à cette box
        self._type=type
        """# @AssociationMultiplicity 1"""

