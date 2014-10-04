class Account:
    def __init__(self, name, account_number, initial_amount, transactions=0):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = transactions

    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1 

    def dump(self):
        s = '%s, %s, balance: %s, transactions: %s' % \
            (self.name, self.no, self.balance, self.transactions)
        print s

    def __iadd__(self, amount):
        self.balance += amount
        self.transactions += 1
        return self

    def __isub__(self, amount):
        self.balance -= amount
        self.transactions += 1
        return self

    def __str__(self):
        s = '%s, %s, balance: %s, transactions: %s' % \
            (self.name, self.no, self.balance, self.transactions)
        return s

    def __repr__(self):
        s = 'Account("%s", "%s", %.2f, %d)' % \
            (self.name, self.no, self.balance, self.transactions)
	return s


def _test():
	a = Account('Noah', '123456789', 100.0)
	a += 200
	a -= 50
	for i in range(100):
		a += 1
	print a # we should have 102 transactions
	s = a.__repr__()
	e = eval(s)
	print e
	

if __name__ == '__main__':
	_test()

'''
python Account3.py
Noah, 123456789, balance: 350.0, transactions: 102
Noah, 123456789, balance: 350.0, transactions: 102
'''
