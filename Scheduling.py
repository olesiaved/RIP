#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Scheduling(object):
	def tri_commande(self) -> None:
		pass

	def __init__(self):
		self._liste_commandes = []
		"""# @AssociationMultiplicity 1..*"""
		self._liste_lignes = []
		"""# @AssociationMultiplicity 1..*"""

