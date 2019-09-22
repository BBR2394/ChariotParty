# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-09-17 13:21:41
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-09-22 23:06:21

#! /usr/local/bin/python3

from interface import *
from random import randint

nbJoueurs = 0
nbTours = 0
nbCases = 0

def gen_case():
	return randint(1,3)

def gen_plate(nb_case):
	board  = []
	for i in range(nb_case):
		board.append(gen_case())
	return board

def gen_gold(nb_case, min):
	return randint(min, nb_case)

def game_loop():
	print("the game loop")
	input("click enter to end the program")

def free_program():
	effacePlateau()

def gen_player(nb_player):
	x = 0
	lst_player = []
	for i in range(x, nb_player):
		lst_player.append({'position' : 0, 'charbon' : 5, 'or' : 0, 'id' : x})
		x += 1
	return lst_player

def checkNumberOfPlayers():
	nbJoueurs = -1
	while nbJoueurs < 0:
		nbJoueurs = inputUInt("How many number of player  between 1 and 4 do you want ?\n-> ")
		if nbJoueurs < 1 or nbJoueurs > 4:
			print("-> incorect nb player, is not valid and must be between 2 and 4")
			nbJoueurs = -1
	return nbJoueurs 

def checkNumberOfTurn():
	nbTours = -1
	while nbTours < 0:
		nbTours = inputUInt("How many turn ? [at least 1] \n-> ")
		if nbTours < 1 :
			print("-> incorect nb player, it is not valid, and must be between 1 and 4")
			nbTours = -1
	return nbTours

def checkNumberOfCases():
	nbCases = -1
	while nbCases < 0:
		nbCases = inputUInt("How many case for the board do you want ? a number divisible by 4 between 4 and 20\n-> ")
		if (nbCases % 4 != 0 or nbCases < 1 or nbCases > 20) and nbCases != -1:
			print("-> incorect nb case : it must be higher than 0, less than 20 and divisible by 4")
			nbCases = -1
	return nbCases

def inputUInt(question):
	nb = input(question)
	try : 
		nb = int(nb)
		return nb
	except ValueError:
		print("please enter a corect number",)
		return -1

def config():
	global nbTours, nbJoueurs, nbCases
	nbJoueurs = checkNumberOfPlayers()
	nbTours = checkNumberOfTurn()
	nbCases = checkNumberOfCases()

def step_two():
	global nbTours, nbJoueurs, nbCases

	config()
	print("Number of turn choosen, number of players, and numbers of cases", nbTours, nbJoueurs, nbCases)
	lst_player = gen_player(nbJoueurs)
	board_game = gen_plate(nbCases)
	gold = gen_gold(nbCases, 1)

	creePlateau(board_game)
	creeJoueurs(lst_player, board_game)
	placeOr(gold, board_game)

	game_loop()
	free_program()

step_two()
