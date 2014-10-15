#this is the class for bank
import sys
import random

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
		
	def createAcc(self, acc, amount):
		self.accounts[acc] = amount
	
	def validateAcc(self, acc):
		if acc in self.accounts.keys():
			return False
		else:
			return True
	
	#implement later
	def transfer(accounts):
		print('transfer')
	