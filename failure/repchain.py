import da
import sys
import random
import configparser
from master import Master
from client import Client
from server import Server
from bank import Bank

def main():
    conf = configparser.ConfigParser()
    conf.read('config')
    da.api.config(channel='fifo', clock='Lamport')
    master = da.api.new(Master, num=int(conf['master']['masterNum']))
    chainNum = int(conf['master']['chainNum'])
    ps = {}
    banks = {}
    bankNames = conf['bank']['bank'].split()
    bankNum = len(bankNames)
    for n in range(1, (bankNum + 1)):
        accounts = {}
        prep = ('bank' + str(n))
        accNum = int(conf[prep]['accountNum'])
        accList = conf[prep]['account'].split()
        amountList = conf[prep]['amount'].split()
        for k in range(1, (accNum + 1)):
            accounts[
            int(accList[(k - 1)])] = int(amountList[(k - 1)])
        bank = Bank(accounts)
        banks[bankNames[(n - 1)]] = bank
    servers = set()
    for n in range(1, (chainNum + 1)):
        prep = ('chain' + str(n))
        serverNum = int(conf[prep]['servers'])
        servBank = conf[prep]['bank']
        ss = da.api.new(Server, num=serverNum)
        servers = (servers | ss)
        ps[servBank] = []
        for s in ss:
            da.api.setup(s, [master, servBank, banks[servBank]])
            ps[servBank].append(s)
    clientNum = int(conf['clients']['number'])
    accList = conf['clients']['acc'].split()
    belongsTo = conf['clients']['chains'].split()
    seedList = conf['clients']['seeds'].split()
    numReqList = conf['clients']['numReq'].split()
    probGetBalanceList = conf['clients']['probGetBalance'].split()
    probDepositList = conf['clients']['probDeposit'].split()
    probTransferList = conf['clients']['probTransfer'].split()
    clients = da.api.new(Client, num=clientNum)
    n = 0
    for c in clients:
        da.api.setup(c, [master, belongsTo[n], 
        int(accList[n]), 
        int(seedList[n]), 
        int(numReqList[n]), (
        float(probGetBalanceList[n]), 
        float(probDepositList[n]), 
        float(probTransferList[n]))])
        n+=1
    print(clients)
    print('\n\n')
    print(ps)
    print('\n\n')
    da.api.setup(master, [ps])
    da.api.start(clients)
    da.api.start(servers)
    da.api.start(master)
