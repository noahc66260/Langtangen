class Account:
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0

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

def _test():
	a = Account('Noah', '123456789', 100.0)
	a.deposit(200)
	a.withdraw(50)
	for i in range(100):
		a.withdraw(1)
	a.dump() # we should have 102 transactions

if __name__ == '__main__':
	_test()

'''
python Account2.py
Noah, 123456789, balance: 150.0, transactions: 102
'''
