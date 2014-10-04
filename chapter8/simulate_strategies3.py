from ndice2 import *
import random
import sys

nrounds = 10**4

def player_guess_modified(ndice):
	return int(3.5*ndice)

ndice_player = 2
ndice_computer = random.randint(2,20)
player = Player('YOU', nrounds, player_guess_modified, ndice_player)
computer = Player('Computer', nrounds, computer_guess, ndice_computer)

for i in range(nrounds):
	player.play_one_round()
	computer.play_one_round()

print 'You used %d dice, computer used %d dice'\
	 % (ndice_player, ndice_computer)
print 'Status: after %g rounds, user has %d euro, machine has %d euros' \
	% (nrounds, player.capital, computer.capital)

if computer.capital > player.capital:
	winner = 'Machine'
else:
	winner = 'You'
print winner, 'won!'

'''
python simulate_strategies3.py
You used 2 dice, computer used 14 dice
Status: after 10000 rounds, user has 13752 euro, machine has 6205 euros
You won!
'''
