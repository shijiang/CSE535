#this is the class for bank
import sys

class Bank():
	def __init__(self, accounts):
		self.accounts = accounts
	
	def getBalance(self,accountNum):
		return self.accounts[accountNum]
		
	def deposit(self,account,amount):
		self.accounts[account] += amount
		return self.accounts[account]
		
	def withdraw(self,account,amount):
		self.accounts[account] -= amount
		return self.accounts[account]	
		
	def createAcc(self, account, amount):
		self.accounts[account] = amount
		
	def transfer(accounts):
		print('transfer')
	