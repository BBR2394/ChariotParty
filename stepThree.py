# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-09-17 13:21:41
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-09-20 15:48:00

#!/usr/local/bin/python3

from interface import *
from random import randint
from time import sleep

nbJoueurs = 0
nbTours = 0
nbCases = 0

glb_lst_player = []
glb_board = []
glb_gold = 0

#to slow the game
glb_timer = 0.1

def gen_case():
	return randint(1,3)

def initalisationPlateau(nb_case):
	board  = []
	for i in range(nb_case):
		board.append(gen_case())
	return board

def gen_gold(nb_case, min):
	return randint(min, nb_case-1)

def free_program():
	effacePlateau()

def intialisationJoueurs(nb_player):
	x = 0
	lst_player = []
	for i in range(x, nb_player):
		lst_player.append({'position' : 0, 'charbon' : 5, 'or' : 0, 'id' : x})
		x += 1
	return lst_player

def checkNumberOfPlayers():
	nbJoueurs = -1
	while nbJoueurs < 0:
		nbJoueurs = inputUInt("Combien de joueurs (entre 1 et 4) voules vous ?\n-> ")
		if nbJoueurs < 1 or nbJoueurs > 4:
			print("-> nombre incorecte : ce doit etre un nombre entre 1 et 4")
			nbJoueurs = -1
	return nbJoueurs 

def checkNumberOfTurn():
	nbTours = -1
	while nbTours < 0:
		nbTours = inputUInt("combien de tour de jeux voulez vous ? Un nombre qui doit etre au moins 1\n-> ")
		if nbTours < 1:
			print("-> nombre de tour incorecte : il doit etre au moins de 1")
			nbTours = -1
	return nbTours

def checkNumberOfCases():
	nbCases = -1
	while nbCases < 0:
		nbCases = inputUInt("Combien de case pour le plateau de jeux voulez vous ? ce doit etre un nombre entre 4 et 20 et doit etre divisible par 4\n-> ")
		if (nbCases % 4 != 0 or nbCases < 1 or nbCases > 20) and nbCases != -1:
			print("-> nombre de case incorecte : il doit etre plus grand que 0, inferieur a 20 et divisible par 4")
			nbCases = -1
	return nbCases

def inputUInt(question):
	nb = input(question)
	try : 
		nb = int(nb)
		return nb
	except ValueError:
		print("entrez un nombre corect",)
		return -1
			
def lanceDe(nbFaces):
	dice = randint(1, nbFaces)
	return dice

def check_buy_gold():
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

def check_same_position_gold_player(lst_player, pos_gold):
	for i in lst_player:
		if i['position'] == pos_gold:
			return False
	return True

def replace_gold():
	global glb_lst_player, glb_gold, glb_board
	while check_same_position_gold_player(glb_lst_player, glb_gold) == False:
		glb_gold = positionGold(len(glb_board))
	placeOr(glb_gold, glb_board)

def acheteLingot(id_player):
	global glb_lst_player, glb_gold, glb_board
	print("vous avez : ", glb_lst_player[id_player]['charbon'], "charbon(s)")
	if glb_lst_player[id_player]['charbon'] < 10:
		print("vous n'avez pas suffisament de charbon, vous ne pouvez pas acheter le lingot :-/")
	else:
		if check_buy_gold():
			glb_lst_player[id_player]['or'] += 1
			glb_lst_player[id_player]['charbon'] -= 10
			replace_gold()

def effetCase(joueur, plateau):
	global glb_lst_player
	if plateau[glb_lst_player[joueur]['position']] == 1: #green +3 
		glb_lst_player[joueur]['charbon'] += 3
	elif plateau[glb_lst_player[joueur]['position']] == 2: #red -3 
		glb_lst_player[joueur]['charbon'] -= 3
		if glb_lst_player[joueur]['charbon'] < 0:
			glb_lst_player[joueur]['charbon'] = 0
	#elif plateau[glb_lst_player[joueur]['position']] == 3: #blue -> nothing

def timer(tm):
	sleep(tm)

# joueur -> id of the player
# nbCases -> number of case to moove
# plateau -> list of the case of the plate
def deplaceJoueur(joueur, nbCases, plateau):
	global nbTours, nbJoueurs
	global glb_lst_player, glb_gold
	global glb_timer

	for i in range(nbCases):
		glb_lst_player[joueur]['position'] += 1
		#to go back to the start case
		if glb_lst_player[joueur]['position'] >= len(plateau):
			glb_lst_player[joueur]['position'] = 0
		bougeJoueur(glb_lst_player[joueur], plateau)
		#if on gold during mooving
		if glb_lst_player[joueur]['position'] == glb_gold:
			acheteLingot(joueur)
		timer(glb_timer)


def tourJoueur(joueur, plateau):
	print("au joueur ", joueur['id'], "de jouer")
	dice_result = lanceDe(6)
	print("resultat du lance de dé => : ", dice_result)
	deplaceJoueur(joueur['id'], dice_result, plateau)
	#event according to the case when the player stop
	effetCase(joueur['id'], plateau)
	
	#if you want to stop the execution until a key triggered
	#input("->wait for the end")

#joueurs -> list of the player
def tourDeJeu(joueurs):
	global glb_board
	for i in joueurs:
		tourJoueur(i, glb_board)

#nbTours -> number of turn
#joueurs -> list of the player
def partie(nbTours, joueurs):
	global glb_lst_player, glb_board, glb_gold
	for j in range(nbTours):
		print("tour : ", j)
		tourDeJeu(glb_lst_player)

def positionGold(nbCases):
	return gen_gold(nbCases, 0)

def configuration():
	global nbTours, nbJoueurs, nbCases
	nbJoueurs = checkNumberOfPlayers()
	nbTours = checkNumberOfTurn()
	nbCases = checkNumberOfCases()

def initialisation():
	global nbTours, nbJoueurs, nbCases
	global glb_lst_player, glb_board, glb_gold
	glb_lst_player = intialisationJoueurs(nbJoueurs)
	glb_board = initalisationPlateau(nbCases)
	glb_gold = positionGold(nbCases)
	creePlateau(glb_board)
	creeJoueurs(glb_lst_player, glb_board)
	placeOr(glb_gold, glb_board)

def print_player_list(lst):
	print("la liste des joueus :")
	for i in lst:
		print(i['id'], " -> ", i)
	print("---------------------------------")

def step_three():
	global nbTours, nbJoueurs
	global glb_lst_player, glb_board, glb_gold
	configuration()
	initialisation()
	partie(nbTours, glb_lst_player)
	#fprint_player_list(glb_lst_player)
	free_program()

step_three()
