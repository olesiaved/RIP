#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Type_produit import Type_produit
from Type_box import Type_box

class Produit(object):
    def SetDateDebutProd(self, aDateDebutProd : int) -> None:
        pass

    def __init__(self):
        self.___dateDebutProd : int = None
        self.___dateFinProd : int = None
        self.___id_commande : int = None
        self.___num_box : int = None
        self._type : Type_produit = None
        """# @AssociationMultiplicity 1"""

    p=Type_produit(1)