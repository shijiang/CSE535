import da
import sys
import random
import configparser
from master import Master
from client import Client
from server import Server
from bank import Bank

def main():
    config = configparser.ConfigParser()
    config.read('config')
    da.api.config(channel='fifo', clock='Lamport')
    banks = []
    accounts = {101: 300, 102: 4000, 103: 200, 104: 30000}
    bank1 = Bank(accounts)
    accounts = {201: 300, 202: 4000, 203: 200, 204: 30000}
    bank2 = Bank(accounts)
    accounts = {301: 300, 302: 4000, 303: 200, 304: 30000}
    bank3 = Bank(accounts)
    accounts = {401: 300, 402: 4000, 403: 200, 404: 30000}
    bank4 = Bank(accounts)
    banks.append(bank1)
    banks.append(bank2)
    banks.append(bank3)
    banks.append(bank4)
    servers = da.api.new(Server, num=4)
    n = 1
    ps = {}
    ps[1] = []
    ps[2] = []
    ps[3] = []
    ps[4] = []
    for server in servers:
        ps[n].append(server)
        n+=1
    n = 1
    for server in servers:
        da.api.setup(server, [n, banks[(n - 1)], ps])
        n+=1
    clients = da.api.new(Client, num=4)
    n = 1
    for client in clients:
        da.api.setup(client, [ps[n][0], ((n * 100) + n)])
        n+=1
    da.api.start(servers)
    da.api.start(clients)
