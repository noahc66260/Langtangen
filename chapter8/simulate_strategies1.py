from ndice2 import *

nrounds = 10**4
ndice = 2
player = Player('YOU', nrounds, player_guess, ndice)
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
python simulate_strategies1.py
Status: after 10000 rounds, user has 13528 euro, machine has 7029 euros
You won!
'''
