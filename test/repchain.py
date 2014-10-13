import da
import sys
import random
from master import Master
from client import Client

def main():
    ps = {}
    nclients = random.randint(0, 9)
    print(('total clients: %i\n' % nclients))
    da.api.config(channel='fifo', clock='Lamport')
    master = da.api.new(Master, num=1)
    da.api.setup(master, [nclients])
    clients = da.api.new(Client, num=nclients)
    da.api.setup(clients, [master])
    n = 0
    for client in clients:
        ps[client] = n
        n+=1
    da.api.start(master)
    da.api.start(clients)
