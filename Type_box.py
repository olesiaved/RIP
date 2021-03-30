#!/usr/bin/python
# -*- coding: UTF-8 -*-

#type de box et caractéristiques
class Type_box(object):

    def __init__(self, t, h, l, p):
        self.type = t       #type de box
        self.hbox = h       #hauteur de la box
        self.lbox = l       #longueur de la box
        self.prix_box = p   # prix de la box

    def affichage(self):
        print ("Type_box", self.type, " ", self.hbox, " ", self.lbox, " ", self.prix_box)