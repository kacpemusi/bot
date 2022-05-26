import requests
import tinydb
from getpass import getpass
from mysql.connector import connect, Error
#https://realpython.com/python-mysql/


# plan for a project:
# setup a database environment
# test security
# test performance
# test transactions
# test in terms of ACID
port = 3306
port2 = 33060
DBpassword = "botprojectbotproject"
username = "adam"
userPass = "adamadamadam"
windowsServiceName = "MySQL80"
databaseName1 = "abcde"
#testuje proste sqli - dwa zadanka ctf
#robi blind sqli kiedy znaleziono podatnosc
#testuje wydatnosc z wielu hostów jednoczesnie


def testDatabase():
    print("TESTING A DATABASE")


def setupDatabase():
    print("SETTING UP A DATABASE CONNECTION")
    try:
        with connect(
                host="localhost",
                user=username,
                password=userPass,
        ) as connection:
            print(connection)
            show_db_query = "create database "+databaseName1
            with connection.cursor() as cursor:
                cursor.execute(show_db_query)
            return connection
    except Error as e:
        print("error")
        print(e)


def welcome():
    with open("welcome.txt", "r") as welc:
        for line in welc.readlines():
            print(line)


def sources():
    with open("sources.txt", "r") as source:
        for line in source.readlines():
            print(line)


def main():
    con = setupDatabase()
    print(con)
    try:
        with connect(
                host="localhost",
                user=username,
                password=userPass,
            database = databaseName1
        ) as connection:
            print(connection)
    except Error as e:
        print("error")
        print(e)


if __name__ == '__main__':
    main()
