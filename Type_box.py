#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Type_box(object):

    def __init__(self, t, h, l, p):
        self.type = t
        self.hbox = h
        self.lbox = l
        self.prix_box = p

    def affichage(self):
        print ("Type_box", self.type, " ", self.hbox, " ", self.lbox, " ", self.prix_box)