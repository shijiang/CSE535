import da
import sys
import random
from master import Master
from client import Client

def main():
    nclients = random.randint(0, 9)
    print(('total clients: %i\n' % nclients))
    da.api.config(channel='fifo')
    master = da.api.new(Master, num=1)
    da.api.setup(master, [nclients])
    clients = da.api.new(Client, num=nclients)
    da.api.setup(clients, [master])
    da.api.start(master)
    da.api.start(clients)
