# In our simplified poker game, a winning hand is that which contains the
# highest ranked card. Thus, we disregard thing such as flushes, straights,
# pairs, etc. If two players have the same highest card, it is a tie.

from scitools.std import *

deck = range(1,14)
deck = append(deck,deck)
deck = append(deck,deck)
random.shuffle(deck)

N = 10**3
nplayers = 5
player_money = zeros(nplayers) + 100
for i in range(N):
	winners = []
	player_money -= 5
	pool = nplayers*5
	random.shuffle(deck)
	player_hands = deck[:nplayers*5]
	winning_card = max(player_hands)
	for j in range(len(player_hands)):
		if winning_card == player_hands[j]:
			if j/nplayers not in winners:
				winners = append(winners,j/nplayers)
	for k in winners:
		player_money[k] += float(pool)/len(winners)

print 'After %g games...' % N
print '%15s %10s' % ('Player Number', 'Money')
for i in range(nplayers):
	print '%15s %10.2f' % (i+1, player_money[i])

'''
python poker.py
After 1000 games...
  Player Number      Money
              1     216.67
              2    -139.58
              3     310.42
              4     -39.58
              5     152.08
'''
