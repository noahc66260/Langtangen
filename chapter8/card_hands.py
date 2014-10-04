from Deck import Deck
from cards import same_rank, same_suit
import random

d = Deck()
N = 10**4
# Probability of two pairs among 5 cards

successes = 0
total = 0
for i in range(N):
	h = d.hand(5)
	if same_rank(h,2) == 2:
		successes += 1
	total += 1
	for j in range(len(h)):
		d.putback(h[j])
	random.shuffle(d.deck)
print 'Probability of two pairs from among 5 cards',
print '%f' % (float(successes)/total)



# Four or five cards of the same suit among 5 cards
successes = 0
total = 0
for i in range(N):
	h = d.hand(5)
	s = same_suit(h)
	for j in s:
		if s[j] == 4 or s[j] == 5:
			successes += 1	
	total += 1
	for j in range(len(h)):
		d.putback(h[j])
	random.shuffle(d.deck)
print 'Probability of four or five cards of the same suit from among 5 cards',
print '%f' % (float(successes)/total)



# four-of-a-kind among five cards
successes = 0
total = 0
for i in range(N):
	h = d.hand(5)
	if same_rank(h,4) == 1:
		successes += 1
	total += 1
	for j in range(len(h)):
		d.putback(h[j])
	random.shuffle(d.deck)
print 'Probability of four-of-a-kind from among 5 cards',
print '%f' % (float(successes)/total)

'''
python card_hands.py
Probability of two pairs from among 5 cards 0.049000
Probability of four or five cards of the same suit from among 5 cards 0.048000
Probability of four-of-a-kind from among 5 cards 0.000400
'''
