#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Type_box import Type_box


class Type_produit(object):
    def __init__(self, a):
        self.___id = a
        self.___s = None
        self.___p = None
        self.___htype = None
        self.___ltype = None
        self.___nbEmpileMax = None
        self._type_box : Type_box = None
    p=Type_box(1,2,3,4)
    
