# -*- coding: utf-8 -*-
# @Author: Baptiste Bertrand-Rapello
# @Date:   2019-09-19 10:08:56
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-09-20 16:15:47

#!/usr/local/bin/python3

from interfaceobjet import *
from random import randint
from time import sleep
from datetime import date, datetime

class Joueur:
	position = 0
	id = 0
	charcoal = 5
	gold = 0

	def __init__(self, idt):
		self.id = idt
		self.position = 0

	def __lt__(self, other):
		char = self.compStuff(self.charcoal, other.charcoal)
		gold = self.compStuff(self.gold, other.gold)
		if gold == -1:
			return True
		elif gold == 0:
			if char == -1:
				return True
			if char == 0:
				return False
			return False

	def __le__(self, other):
		char = self.compStuff(self.charcoal, other.charcoal)
		gold = self.compStuff(self.gold, other.gold)
		if gold == -1:
			return True
		elif gold == 0:
			if char == -1:
				return True
			if char == 0:
				return True
			return False

	def __eq__(self, other):
		if (self.gold == other.gold) and (self.charcoal == other.charcoal):
			return True
		return False

	def __ne__(self, other):
		if (self == other):
			return False
		else :
			return True
		return False

	def __gt__(self, other):
		char = self.compStuff(self.charcoal, other.charcoal)
		gold = self.compStuff(self.gold, other.gold)
		
		if gold == 1:
			return True
		elif gold == 0:
			if char == 1:
				return True
			if char == 0:
				return False
			else :
				return False

	def __ge__(self, other):
		char = self.compStuff(self.charcoal, other.charcoal)
		gold = self.compStuff(self.gold, other.gold)
		
		if gold == 1:
			return True
		elif gold == 0:
			if char == 1:
				return True
			if char == 0:
				return True
			else :
				return False

	def compStuff(self, stuff1, stuff2):
		if stuff1 > stuff2:
			return 1
		elif stuff1  < stuff2:
			return -1
		return 0

	def setChar(self, newChar):
		self.charcoal = newChar

	def setGold(self, newGold):
		self.gold = newGold

	def getChar(self):
		return self.charcoal

	def getGold(self):
		return self.gold

	def getId(self):
		return self.id

	def getPosition(self):
		return self.position

	def setPosition(self, newPos):
		self.position = newPos

	def incrementPosition(self):
		self.position += 1

	def boughtGold(self):
		self.charcoal -= 10
		self.gold += 1

class Case:
	couleur = 0

	def __init__(self):
		self.couleur = 0
		self.nom = ''
		self.bonus = 0

	def effet(self, joueur):
		return False

	def getType(self):
		return self.couleur

	def getNom(self):
		return self.nom

class CaseJaune(Case):
	def __init__(self):
		self.couleur = 4 
		self.bonus = 10
		self.nom = 'Jaune'
		print("je viens detre initialisé et je suis une case : ", self.nom, "  de bonus : ", self.bonus)

	def effet(self, joueur):
		joueur.setChar(joueur.getChar() + self.bonus)
		print("dans l'effet de la case : ", self.nom)
		return True

class CaseBleu(Case):

	def __init__(self):
		self.couleur = 3 
		self.bonus = 0
		self.nom = 'Bleu'
		print("je viens detre initialisé et je suis une case : ", self.nom, "  de bonus : ", self.bonus)

	def effet(self, joueur):
		joueur.setChar(joueur.getChar() + self.bonus)
		print("dans l'effet de la case : ", self.nom)
		return True

class CaseRouge(Case):

	def __init__(self):
		self.couleur = 2
		self.bonus = -3
		self.nom = 'Rouge'
		print("je viens detre initialisé et je suis une case : ", self.nom, "  de bonus : ", self.bonus) 

	def effet(self, joueur):
		temp_char = joueur.getChar() + self.bonus
		if temp_char < 0:
			joueur.setChar(0)
		else:
			joueur.setChar(joueur.getChar() + self.bonus)
		print("dans l'effet de la case : ", self.nom)
		return True

class CaseVerte(Case): 

	def __init__(self):
		self.couleur = 1
		self.bonus = 0
		self.nom = 'Verte'
		print("je viens detre initialisé et je suis une case : ", self.nom, "  de bonus : ", self.bonus)

	def effet(self, joueur):
		joueur.setChar(joueur.getChar() + self.bonus)
		print("dans l'effet de la case : ", self.nom)
		return True

class FabriqueCase:
	maxType = 4
	lstFunctionCreate = []

	def __init__(self):
		print("dans fabrique case")
		self.lstFunctionCreate.append(self.createGreenCase())
		self.lstFunctionCreate.append(self.createRedCase())
		self.lstFunctionCreate.append(self.createBlueCase())
		self.lstFunctionCreate.append(self.createYellowCase())

	#soit on envoie 0 et on genere le nombre entre 1 et maxType
	#soit on envoie un autre nombre qui est généré par le plateau
	def create(self, color):
		if color == 0:
			gen = randint(1, self.maxType)
		else :
			gen = color
		return self.lstFunctionCreate[gen-1]

	def createGreenCase(self):
		print("je cree une case verte")
		return CaseVerte()

	def createRedCase(self):
		print("je cree une case rouge")
		return CaseRouge()

	def createBlueCase(self):
		print("je cree une case bleu")
		return CaseBleu()

	def createYellowCase(self):
		print("je cree une case jaune")
		return CaseJaune()

class Plateau:
	lstCase = []
	lstJoueur = []
	pos_gold = 0
	number_turn = 0
	number_player = 0
	number_case = 0
	factory = None
	the_timer = 0.01

	def __init__(self, nbTours, nbJoueurs, nbCases):
		self.number_turn = nbTours
		self.number_player = nbJoueurs
		self.number_case = nbCases
		self.factory = FabriqueCase()
		self.initBoard()
		self.initPlayer()
		self.initGold()
		self.createBoard()


	def initBoard(self):
		for i in range(self.number_case):
			self.lstCase.append(self.factory.create(0))
			#self.lstCase.append(self.factory.create(self.gen_case(0)))
			#self.addCase()
		print("le plateau est composé de ", self.plateSize(), " cases")

	def initPlayer(self):
		for i in range(self.number_player):
			self.lstJoueur.append(Joueur(i))
			print("-> joueur ", i, " créé")

	def gen_gold(self, seed, min):
		return randint(min, self.number_case - 1)

	def initGold(self):
		#initialisation de l'or
		self.pos_gold = self.gen_gold(0, 0)

	def createBoard(self):
		creePlateau(self.lstCase)
		creeJoueurs(self.lstJoueur, self.lstCase)
		placeOr(self.pos_gold, self.lstCase)

	#pour generer un nombre entre 1 et 3 
	def gen_case(self, seed):
		return randint(1,3)

	def plateSize(self):
		return len(self.lstCase)

	def lanceDe(self, nbFaces):
		dice = randint(1, nbFaces)
		return dice

	def check_same_position_gold_player(self):
		for i in self.lstJoueur:
			if i.getPosition() == self.pos_gold:
				return False
		return True	

	def replace_gold(self):
		while self.check_same_position_gold_player() == False:
			self.gold =  self.initGold()
		placeOr(self.pos_gold, self.lstCase)

	def check_buy_gold(self):
		answer_possible_ok = ['Oui', 'Yes']
		answer_possible_not_ok = ['Non', 'No']
		check_answer = False
		while check_answer == False:
			answer = input("voulez vous acheter le lingot [Oui:Non]\n-> ")
			check_answer = answer in answer_possible_ok
			if check_answer == True:
				return True
			if check_answer == False:
				check_answer = answer in answer_possible_not_ok
				if check_answer == True:
					return False


	def acheteLingot(self, idJoueur):
		print("vous avez :", self.lstJoueur[idJoueur].getChar(), " charbon(s)")
		if self.lstJoueur[idJoueur].getChar() < 10:
			print("vous n'avez pas suffisament de charbon, vous ne pouvez pas acheter le lingot :-/")
		else:
			if self.check_buy_gold():
				self.lstJoueur[idJoueur].boughtGold()
				self.replace_gold()

	def timer(self, tm):
		sleep(tm)

	# joueur -> id of the player
	# nbCases -> number of case to moove
	def deplaceJoueur(self, idJoueur, nbCases):
		print("in deplaceJoueur function : ", self.number_case, " player n° ", idJoueur, " number of case to moove : ", nbCases)
		for i in range(nbCases):
			self.lstJoueur[idJoueur].incrementPosition()
			#to go back to the start case
			if self.lstJoueur[idJoueur].getPosition() >= self.number_case:
				self.lstJoueur[idJoueur].setPosition(0)
			bougeJoueur(self.lstJoueur[idJoueur], self.lstCase)
			#if on gold during mooving
			if self.lstJoueur[idJoueur].getPosition() == self.pos_gold:
				self.acheteLingot(idJoueur)
			self.timer(self.the_timer)

	def tourJoueur(self, joueur):
		dice_result = self.lanceDe(6)
		print("Le resultat du de\n-> : ", dice_result)
		#deplaceJoueur -> moove the player
		self.deplaceJoueur(joueur.getId(), dice_result)
		#.effet() -> event according to the case when the player stop
		self.lstCase[joueur.getPosition()].effet(joueur)

	def tourDeJeu(self):
		for i in self.lstJoueur:
			self.tourJoueur(i)

	def partie(self):
		turn_x = 0
		for j in range(self.number_turn):
			print("turn : ", turn_x)
			self.tourDeJeu()
			turn_x += 1

	def compJoueursObj(self, joueur1, joueur2):
		if joueur1 <= joueur2:
			return True 
		else:
			return False

	def triJoueurs(self):
		if len(self.lstJoueur) <= 1:
			return True
		i = 0
		while i < len(self.lstJoueur)-1:
			rtr = self.compJoueursObj(self.lstJoueur[i], self.lstJoueur[i+1])
			if self.compJoueursObj(self.lstJoueur[i], self.lstJoueur[i+1]) == False:
				first = self.lstJoueur.pop(i)
				second = self.lstJoueur.pop(i)
				self.lstJoueur.insert(i, first)
				self.lstJoueur.insert(i, second)
				i = 0
			else :
				i += 1

	def afficheClassement(self):
		today = date.today()
		nb_player = len(self.lstJoueur)
		for i in self.lstJoueur:
			print("Numéro " + str(nb_player) + "  : Joueur  " + str(i.id + 1) + "  avec  " + str(i.gold) + "  lingot(s) d'or et  " + str(i.charcoal) + " charbon(s)")
			nb_player -= 1

	def open_a_file(self, file_name):
		try:
			fd = open(file_name, 'w')
			print("le fichier a ete ouvert")
			return fd
		except  :
			print("an error occured when opening/creating the file")
			return -1

	def sauvegardeResultats(self):
		today = datetime.today()
		nb_player = len(self.lstJoueur)
		file_name = "chariot-party-" + '{:02d}'.format(today.day) + "-" + '{:02d}'.format(today.month) + "-" + str(today.year) + "-" + '{:02d}'.format(today.hour) + "-" + '{:02d}'.format(today.minute) + ".txt"
		grading = ""
		for i in self.lstJoueur:
			grading += "Numéro " + str(nb_player) + "  : Joueur  " + str(i.getId() +1) + "  avec  " + str(i.getGold()) + "  lingot(s) d'or et  " + str(i.getChar()) + " charbon(s)" + '\n'
			nb_player -= 1	
		fd = self.open_a_file(file_name)
		if fd != -1:
			fd.write(grading)
			fd.close()

	def endGame(self):
		self.triJoueurs()
		self.afficheClassement()
		self.sauvegardeResultats()
		effacePlateau()

	def play(self):
		self.partie()
		self.endGame()

class Configuration:
	nbTours = 0
	nbJoueurs = 0
	nbCases = 0

	def __init__(self):
		print("configuration created")
		self.checkNumberOfPlayers()
		self.checkNumberOfTurn()
		self.checkNumberOfCases()

	def checkNumberOfCases(self):
		self.nbCases = -1
		while self.nbCases < 0:
			self.nbCases = self.inputInt("Combien de case pour le plateau de jeux voulez vous ? ce doit etre un nombre entre 4 et 20 et doit etre divisible par 4\n-> ")
			if (self.nbCases % 4 != 0 or self.nbCases < 1 or self.nbCases > 20) and self.nbCases != -1:
				print("-> nombre de case incorecte : il doit etre plus grand que 0, inferieur a 20 et divisible par 4")
				self.nbCases = -1
		return self.nbCases

	def checkNumberOfPlayers(self):
		self.nbJoueurs = -1
		while self.nbJoueurs < 0:
			self.nbJoueurs = self.inputInt("Combien de joueurs (entre 1 et 4) voules vous ?\n-> ")
			if self.nbJoueurs < 1 or self.nbJoueurs > 4:
				print("-> nombre  de joueurs incorecte : ce doit etre un nombre entre 1 et 4")
				self.nbJoueurs = -1
		return self.nbJoueurs 

	def checkNumberOfTurn(self):
		self.nbTours = -1
		while self.nbTours < 0:
			self.nbTours = self.inputInt("Combien de tour de jeux voulez vous ? Un nombre qui doit etre au moins 1\n-> ")
			if self.nbTours < 1:
				print("-> nombre de tour incorecte : il doit etre au moins de 1")
				self.nbTours = -1
		return self.nbTours
	
	def inputInt(self, question):
		nb = input(question)
		try : 
			nb = int(nb)
			return nb
		except ValueError:
			print("entrez un nombre corect",)
			return -1

	def getNbTour(self):
		return self.nbTours

	def getNbJoueur(self):
		return self.nbJoueurs

	def getNbCases(self):
		return self.nbCases


def main():	
	print("step Five")
	config = Configuration()
	game = Plateau(config.getNbTour(), config.getNbJoueur(), config.getNbCases())
	game.play()

main()