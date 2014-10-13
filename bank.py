#this is the class for bank
import sys

class Bank():
	def __init__(self, accounts):
		self.accounts = accounts
	
	def getBalance(accountNum):
		return accounts[accountNum]
		
	def deposit(account):
		accounts[account[0]] =+ account[1]
		return accounts[account[0]]
		
	def withdraw(account):
		accounts[account[0]] =-account[1]
		return accounts[account[0]]	
		
	def transfer(accounts):
		print('transfer')
	