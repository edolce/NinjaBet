import json

import requests
import cloudscraper
scraper = cloudscraper.create_scraper()

def get_ssoid():

    data = {
        'product': 'exchange-eds',
        'redirectMethod': 'GET',
        'url': 'https://www.betfair.it/exchange/plus/?loginStatus=SUCCESS&ott=XMrVK6jTh8RnCK8tX6IofhOWJSEmybKq5kEaQsqETWkHIlRkWmEAy%2BhH19x40tHQ',
        'submitForm': 'true',
        'tmxId': '0003896d-f7d6-4b9e-b533-c5e2d3b96990',
        'username': 'edoardoguani@yahoo.it',
        'password': 'Nutella00#',
    }

    info = scraper.post('https://identitysso.betfair.it/api/login', data=data)


    return info.cookies.get_dict()


def get_betfair_bets(cookies):

    headers = {
        'authority': 'myactivity.betfair.it',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json;charset=UTF-8',
        # 'cookie': 'vid=dd3e0e5b-7a9b-4392-98e5-8bfd20bbd834; storageSSC=lsSSC%3D1; StickyTags=rfr=3013; language=it; rfr=980047; pi=partner980047; PI=980047; TrackingTags=rfr=980047; OptanonAlertBoxClosed=2023-10-04T19:59:04.677Z; _gcl_au=1.1.777076877.1696449545; _scid=bd9a22c3-87b9-4ded-bd77-b621f857eb9f; bfsd=ts=1696449546242|st=reg; ccawa=3312373556307386367626832208248461633602; betexPtk=betexLocale%3Dit%7EbetexRegion%3DGBR%7EbetexCurrency%3DEUR; wsid=57146ef0-6ffd-11ee-8201-fa163ed14ea5; betexPtkSess=betexLocaleSessionCookie%3Dit%7EbetexRegionSessionCookie%3DGBR; _gid=GA1.2.1326804054.1698303257; BETEX_ESD=accountservices; xsrftoken=ed2b8b30-73db-11ee-9b45-fa163e0bac6d; exp=ex; _ga_7YVN2PDRZW=GS1.2.1698386267.2.0.1698386267.0.0.0; ssoid=OKG8M97cLhNnzb2XRR/+ulJT8PhyB9GUMRsk1+PeIxc=; loggedIn=true; Qualtrics_Cookie=61633602; __cf_bm=9Sfc9CK4sD184tV148VYIXVObeFOl4Uywfwhd1osTqM-1698402505-0-AW8Tn2+BsTLjIpWElsxTzC9ozPXRo/65LRWPp0C0hvRKdn+YlrzOOwzEUelKaMQK4qpTsblExsILRH4sB1Tz/ZY=; lka=1698402600748; gtmfl=G8M97; cf_clearance=eWC9uBTIQlM_1zEl4RmQ2g0zzpawfhQ4WIo9.RBk974-1698402624-0-1-87d446c4.87801de4.c3b5501b-0.2.1698402624; TEAL=v:418afc45c21d37258998654003391576f4925674bb8$t:1698404425692$sn:9$en:1$s:1698402625690%3Bexp-sess; _ga_K0W97M6SNZ=GS1.1.1698402625.9.0.1698402625.60.0.0; _ga=GA1.2.574887657.1696449545; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Oct+27+2023+12%3A30%3A35+GMT%2B0200+(Ora+legale+dell%E2%80%99Europa+centrale)&version=6.18.0&isIABGlobal=false&hosts=&consentId=61633602&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=%3B&AwaitingReconsent=false; _scid_r=bd9a22c3-87b9-4ded-bd77-b621f857eb9f; _uetsid=7af72cb073cc11eeb89473ef5de66f22; _uetvid=787fbfc062f011eeb0a3df382d003a2e; _gat=1',
        'origin': 'https://myactivity.betfair.it',
        'referer': 'https://myactivity.betfair.it/exchange',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    json_data = {
        'status': 'SETTLED',
        'fromRecord': 0,
        'pageSize': 100,
        'selectedBets': 'MAIN',
        'state': 'SETTLED',
        'eventTypeId': None,
        'dateFilter': '90',
        'startDate': None,
        'endDate': None,
    }

    response = scraper.post(
        'https://myactivity.betfair.it/activity/exchange/settled',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )


    # update cookies file
    with open("cookies_Betfair.JSON", "w") as f:
        json.dump(cookies, f)

    return response.json()


def main():
    # get cookies from William Hill Cookies file
    with open("cookies_Betfair.JSON", "r") as f:
        cookies = json.load(f)

    try:
        return get_betfair_bets(cookies)
    except Exception as e:
        cookies = get_ssoid()
        return get_betfair_bets(cookies)



