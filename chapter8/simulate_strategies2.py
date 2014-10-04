from ndice2 import *
import sys

nrounds = 10**4
ndice = int(sys.argv[1])

def player_guess_modified(ndice):
	return int(3.5*ndice)

player = Player('YOU', nrounds, player_guess_modified, ndice)
computer = Player('Computer', nrounds, computer_guess, ndice)

for i in range(nrounds):
	player.play_one_round()
	computer.play_one_round()

print 'Status: after %g rounds, user has %d euro, machine has %d euros' \
	% (nrounds, player.capital, computer.capital)

if computer.capital > player.capital:
	winner = 'Machine'
else:
	winner = 'You'
print winner, 'won!'

'''
python simulate_strategies2.py 3
Status: after 10000 rounds, user has 13134 euro, machine has 7118 euros
You won!

python simulate_strategies2.py 50
Status: after 10000 rounds, user has 56496 euro, machine has 8437 euros
You won!
'''
