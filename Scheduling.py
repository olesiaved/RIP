#!/usr/bin/python
# -*- coding: UTF-8 -*-
from operator import attrgetter

from Box_manager import Box_manager

# classe de gestion des production de toutes les commandes, produits, attribution de box et gestion des boxs
# 2nd classe principale après la classe Production
class Scheduling(object):

	def __init__(self):
		self._liste_commandes = []
		"""# @AssociationMultiplicity 1..*"""
		"""# @AssociationMultiplicity 1..*"""
		self._liste_lignes = []
		"""# @AssociationMultiplicity 1..*"""
		self.box_manager = Box_manager()
		"""# @AssociationMultiplicity 1"""




# repartition des commandes entre les lignes de production à disposition

	def TriCommande(self,ListCommande):
		# ENSEMBLE DES COMMANDES A AJOUTER CONSIDEREE
		LigneReference = self._liste_lignes[0]

		for LocalCom in ListCommande:
			BestDelayLine=-1

		# ENSSEMBLE DES LIGNES DE PROD DU SCHEDULER CONSIDEREES
			for LocalLigne in self._liste_lignes:
				LocalDelayLine = 0

		# ETAPE 1: CALCUL DU DELAIS EN FONCTION DE TOUTES LES COMMANDES DEJA PLACEE SUR LA LIGNE
				for LocalCommande in LocalLigne._listes_commandes:
					for LocalProduit in  LocalCommande._liste_produits_afaire :
						LocalDelayLine = LocalDelayLine + LocalProduit._type.p


		# ETAPE 2: CHOIX DE LA LIGNE OU LE DELAI EST LE PLUS FAIBLE
				if(LocalDelayLine<BestDelayLine) or (BestDelayLine==-1):
					BestDelayLine=LocalDelayLine
					LigneReference=LocalLigne

			LocalCom._num_ligne = LigneReference._numero
			LigneReference._listes_commandes.append(LocalCom)

		# ici je remplis produit a faire pour chaque ligne
		for i in self._liste_lignes:
			for j in i._listes_commandes:
				for k in j._liste_produits_afaire:
					i._produits_afaire.append(k)



	def TriProduit(self,ListTypeProd):
		print("run")
		ListTypeProd = self.box_manager._listes_types_produit
		ListTraitementCommande = []

		#ORDONANCEMENT DES COMMANDES EN FONCTION DE LA DATE DE LIVRAISON ATTENDUE


		# ORDONNANCEMENT DES COMMANDES EN FONCTION DU RATIO [ taxe /  taxe durée ]

		while (len(ListTraitementCommande) < len(self._liste_commandes)):
			LocalVar = -1
			minimumLoc = self._liste_commandes[0]

			for i in (self._liste_commandes):
				if (i not in ListTraitementCommande):
					if (LocalVar == -1):
						minimumLoc = i
						LocalVar = 0

					if (i._penalite  <= minimumLoc._penalite ):
						minimumLoc = i

			minimumLoc.affichage()
			ListTraitementCommande.append(minimumLoc)

		#	for ii in ListTraitementCommande:
		#		ii.

		for i in ListTraitementCommande:
			self.FastestLineGivenOrder(i, ListTypeProd)

	"""
			while(len(ListTraitementCommande)<len(self._liste_commandes)):
				LocalVar= -1
				minimumLoc=self._liste_commandes[0]
				for i in (self._liste_commandes):

					if(i not in ListTraitementCommande):
						if(LocalVar==-1):
							minimumLoc=i
							LocalVar=0

						if(i._datePrevue<=minimumLoc._datePrevue):
							minimumLoc=i

				minimumLoc.affichage()
				ListTraitementCommande.append(minimumLoc)

			#	for ii in ListTraitementCommande:
			#		ii.

			for i in ListTraitementCommande:
				self.FastestLineGivenOrder(i,ListTypeProd)
	"""

	def FastestLineGivenOrder(self,ORDER,ListTypeProd):
		TypePreviousProd = None
		PreviousLine = None


		for pdtype in ListTypeProd:
			#statutAttribution=0
			for products in ORDER._liste_produits_afaire:
				if(products._type==pdtype):
					if(PreviousLine!=None):
						if(TypePreviousProd != None):
							if(TypePreviousProd == products._type):
								# SI LE DERNIER PRODUIT EST DU TYPE DU PRODUIT ACTUEL : PRENDRE LA MEME LIGNE SI CELA PERMET DE RESPECT LE TEMPS DE PROD
						#SINON PRENDRE LA LIGNE AVEC LE DELAIS D'ATTENTE LE PLUS FAIBLE
								if (PreviousLine.LocalDelay + products._type.p <= ORDER._datePrevue ):#and statutAttribution==0):
									PreviousLine.AddProdAfaire(products)

								elif (PreviousLine.LocalDelay + products._type.p > ORDER._datePrevue):
									PreviousLine = self.FastestLineGivenProduct(products)
			# SI LE DERNIER PRODUIT REALISE N'EST PAS DU TYPE DU PRODUIT ACTUEL : PRENDRE LA LIGNE AVEC LE DELAIS MINIMUM
							elif(TypePreviousProd != products._type):
								PreviousLine = self.FastestLineGivenProduct(products)

				# SI AUCUN PRODUIT DE LA COMMANDE ACTUELLE N'A ETE FAIT: PRENDRE LA LIGNE AVEC LE DELAIS MINIMUM
						else:
							PreviousLine = self.FastestLineGivenProduct(products)

					else:
						PreviousLine =self.FastestLineGivenProduct(products)


				TypePreviousProd=products._type




	def FastestLineGivenProduct(self, PRODTEST):
		BestDelayLine = None
		LigneReference= None

		for LocalLigne in self._liste_lignes:
		# ETAPE 2: CALCUL DU  NOUVEAU DELAIS EN CAS D'AJOUT DU PRODUIT CONSIDERE SUR LA LIGNE
			if(LocalLigne.LastestProdAdded==PRODTEST._type):
				LocalDelayLine = LocalLigne.LocalDelay + PRODTEST._type.p

			elif (LocalLigne.LastestProdAdded != PRODTEST._type):
				LocalDelayLine = LocalLigne.LocalDelay + PRODTEST._type.p + PRODTEST._type.s

		# ETAPE 2: CHOIX DE LA LIGNE OU LE DELAI EST LE PLUS FAIBLE
			if(BestDelayLine!=None):
				if((LocalDelayLine<BestDelayLine) or (LigneReference==None)):
					BestDelayLine=LocalDelayLine
					LigneReference=LocalLigne

			elif(BestDelayLine==None):
				BestDelayLine = LocalDelayLine
				LigneReference = LocalLigne



		LigneReference.AddProdAfaire(PRODTEST)
		return LigneReference

		# ici je remplis produit a faire pour chaque ligne
		for i in self._liste_lignes:
				for j in i._listes_commandes:
					for k in j._liste_produits_afaire:
						i._produits_afaire.append(k)



	def InitialasiationTri(self):
		self. TriProduit(self._liste_commandes)

	def AffichageEtatCommande(self):
		for element in self._liste_commandes:
			element.affichage()

	def AffichageEtatLignes(self):
		for element in self._liste_lignes:
			element.affichage()




# production de toutes les commandes de chaque ligne
	def calcul_date_prod(self):
		for i in self._liste_lignes:
			i.calcul_date_produit_opt()



# Calcul de la date réelle d'envoie pour chaque commande

	def date_fin_prod(self):
		for element in self._liste_commandes:
			element.DateEnvoieFin()

	def recherche_date_suivante(self):
		date = 0
		stop = False
		min = 0
		while (stop == False):
			liste = []
			for i in self._liste_lignes:
				liste.append(i.recherche_date_suivante(date))
				liste = list(filter(None, liste))
					# for k in liste:
					# k.affichage()
				if liste != []:
					min = liste[0]
					for k in liste:
						if k._dateFinProd < min._dateFinProd:
							min = k
					self.box_manager.gestion_produit_finis(min)
					date = min._dateFinProd
				else:
					stop = True

				""" 
# Attribution d'un numero de box pour chaque produit
	def numero_box_pour_produit(self):
		self.box_manager._listes_box=[0]*len(self.box_manager._listes_types_box)
		for i in self._liste_lignes:
			for j in i._listes_commandes:
				for k in j._liste_produits_finis:
					self.box_manager.Achat_Box_Type(k)
					
				"""



""" 	def DelayLine(self,ligne):
		LocalDelayLine=0
		LocalVarm = 0
		LocalVaro = 0
		for LocalVarm in  range(len(ligne._listes_commandes)):
			for LocalVaro in range(len(ligne._listes_commandes[LocalVarm]._liste_produits_afaire)):
				LocalDelayLine=LocalDelayLine+Ligne._listes_commandes[LocalVarm]._liste_produits_afaire[LocalVaro]._type.p

		return


	def tri_commande(self):
		# gives us the fastest line
		IndexFastestLine = 0
		LocalDelayReference = self.DelayLine(self._liste_lignes[0])
		LocalVaru =0
		localDelay = 0
		for LocalVaru in range(len(self._liste_lignes)):
			localDelay = self.DelayLine(self._liste_lignes[LocalVaru])

			if(LocalDelayReference >localDelay):
				LocalDelayReference=localDelay
				IndexFastestLine=LocalVaru

"""





