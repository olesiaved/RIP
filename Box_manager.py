#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Box import Box
from Type_box import Type_box
from Type_produit import Type_produit

class Box_manager(object):
    def Attribution_type(self):
        for i in self._listes_types_produit:
            b = Type_box("B", 1000000, 1000000, 1000000)
            for j in self._listes_types_box:
                if i.htype<=j.hbox and i.ltype<=j.lbox and j.prix_box<b.prix_box :
                    b=j
            i.type_box=b



    def Available_Box_Type(self, aBB ) :
        pass

    def Achat_Box_Type(self, p ):
        i=self._listes_types_box.index(p._type.type_box)
        self._listes_box[i]+=1
        p._num_box=self._listes_box[i]

    def __init__(self):
        self._listes_box = []
        self._listes_types_produit = []
        self._listes_types_box = []


    
    