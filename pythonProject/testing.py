from mysql.connector import connect, Error
from socket import *
port = 3306
port2 = 33060
DBpassword = "botprojectbotproject"
username = "adam"
userPass = "adamadamadam"
windowsServiceName = "MySQL80"
databaseName1 = "abcde"
host = "localhost"

if __name__ == '__main__':
        print("SETTING UP A DATABASE CONNECTION")
        show_db_query = b"create database abcde"
        socket = socket(AF_INET, SOCK_STREAM)
        socket.connect((host, port))
        while True:
            socket.send(show_db_query)
            print("command sent")
        socket.send(show_db_query)
        print("sent again")
        try:
            with connect(
                    host="localhost",
                    user=username,
                    password=userPass,
            ) as connection:
                print(connection)
                with connection.cursor() as cursor:
                    cursor.execute(show_db_query)
                #return connection
        except Error as e:
            print("error")
            print(e)