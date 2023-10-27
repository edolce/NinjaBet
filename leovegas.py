import datetime
import json

import requests
def get_token():
    cookies = {
        'visid_incap_1705993': 'KAlAhUV5TMS9GzUMov4vbVANOmUAAAAAQUIPAAAAAABJ1W8ww/BIQl6HLL/W77tM',
        'nlbi_1705993': 'zlWUe2WuvjrzrkQw9tXEVgAAAABs/To2NzHMqvoAzvWWX8vS',
        'incap_ses_477_1705993': 'UcK/cLRtcm7COJtW1qaeBlANOmUAAAAATxH1vJZlPjd5qtK9rbLeYQ==',
        'FPID': 'FPID2.2.8mypsk%2FZEzTjeqldQQufzxa59glgEdC1Y7omqHbaav4%3D.1698303318',
        '_gcl_au': '1.1.416797156.1698303318',
        'FPAU': '1.2.1204045000.1698303317',
        'data': '5f71c28f511989bbfc16e012f96c37af',
        'leo-essentials': '%7B%22cid%22%3A%2202c48cb8-0d1c-4a3c-b390-4bdc49dc3c2a%22%2C%22rc%22%3Atrue%7D',
        '_ga': 'GA1.2.336119500.1698303318',
        'FPLC': 'xcdbUJh2saSKX2XWoYxeFtcHzIZiNoKKConp7trd1bgNchkUYPzNiibHLqlbF7W%2B0GA5YyzRlRJGAFPVSgx48u5mUuNDLsKOEWGbxai9TLZ%2B5%2F1KrGjE2KfWtwyEug%3D%3D',
        'leo-sid': 's%3Alags-jKOu96IUCnSLN4anPIGN5zY-EBpJ31rB.Zwh%2BWgqa8T8WK%2BpPGb7FxDJb%2FzQjCXcHGpFzhCu%2Bf4I',
        '_gat_leo': '1',
        '_gat_sportsbookv3': '1',
        'leo_previous_page': 'https://www.leovegas.it/it-it/login',
        '_ga_B4STQPNQJ2': 'GS1.1.1698404735.2.1.1698404897.0.0.0',
        '_dd_s': 'rum=1&id=94d8b357-bbfe-4913-9e5d-213a86067d49&created=1698404735508&expire=1698405801845',
    }

    headers = {
        'authority': 'www.leovegas.it',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'visid_incap_1705993=KAlAhUV5TMS9GzUMov4vbVANOmUAAAAAQUIPAAAAAABJ1W8ww/BIQl6HLL/W77tM; nlbi_1705993=zlWUe2WuvjrzrkQw9tXEVgAAAABs/To2NzHMqvoAzvWWX8vS; incap_ses_477_1705993=UcK/cLRtcm7COJtW1qaeBlANOmUAAAAATxH1vJZlPjd5qtK9rbLeYQ==; FPID=FPID2.2.8mypsk%2FZEzTjeqldQQufzxa59glgEdC1Y7omqHbaav4%3D.1698303318; _gcl_au=1.1.416797156.1698303318; FPAU=1.2.1204045000.1698303317; data=5f71c28f511989bbfc16e012f96c37af; leo-essentials=%7B%22cid%22%3A%2202c48cb8-0d1c-4a3c-b390-4bdc49dc3c2a%22%2C%22rc%22%3Atrue%7D; _ga=GA1.2.336119500.1698303318; FPLC=xcdbUJh2saSKX2XWoYxeFtcHzIZiNoKKConp7trd1bgNchkUYPzNiibHLqlbF7W%2B0GA5YyzRlRJGAFPVSgx48u5mUuNDLsKOEWGbxai9TLZ%2B5%2F1KrGjE2KfWtwyEug%3D%3D; leo-sid=s%3Alags-jKOu96IUCnSLN4anPIGN5zY-EBpJ31rB.Zwh%2BWgqa8T8WK%2BpPGb7FxDJb%2FzQjCXcHGpFzhCu%2Bf4I; _gat_leo=1; _gat_sportsbookv3=1; leo_previous_page=https://www.leovegas.it/it-it/login; _ga_B4STQPNQJ2=GS1.1.1698404735.2.1.1698404897.0.0.0; _dd_s=rum=1&id=94d8b357-bbfe-4913-9e5d-213a86067d49&created=1698404735508&expire=1698405801845',
        'origin': 'https://www.leovegas.it',
        'referer': 'https://www.leovegas.it/it-it/login',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-leo-locale': 'it-it',
        'x-request-id': 'ea6d8c98-2534-4b94-810e-2adfcc5931ee',
    }

    json_data = {
        'operationName': 'LoginWithPasswordMutation',
        'query': 'mutation LoginWithPasswordMutation(\n  $input: LoginWithPasswordInput!\n) {\n  loginWithPassword(input: $input) {\n    viewer {\n      authenticated\n      locale {\n        string\n      }\n      unixTimestamp\n      user {\n        userId\n        clientIP\n        license {\n          name\n        }\n        balance {\n          amount\n          fetchedAt\n          totalBonusCasino\n          pendingWithdrawal {\n            amount\n          }\n        }\n        country {\n          code\n          tncVersion\n          id\n        }\n        currency\n        details {\n          nickname\n          firstName\n          lastName\n          gender\n          dateOfBirth\n          mobileNumber\n          mobileNumberPrefix\n          address {\n            city\n            zip\n          }\n        }\n        stats {\n          latestLogin\n          created\n          isPasswordExpired\n        }\n        pendingDocumentationRequests {\n          verifiedUntil\n        }\n        acceptedTnC\n        status\n        thirdPartyAccounts {\n          provider\n        }\n        id\n      }\n      id\n    }\n  }\n}\n',
        'variables': {
            'input': {
                'password': 'Lucetta3#',
                'username': 'piumarg@yahoo.it',
                'blackbox': 'Web;75eacdcf-d366-48a5-bbd1-7de16813c11d;rQBMRJiRwZsGfQebqa2Zdg==;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',
            },
        },
    }

    response = requests.post('https://www.leovegas.it/api?relay', cookies=cookies, headers=headers, json=json_data)

    print("cookie_status",response.status_code)
    print("cookie_text",response.text)
    return response.cookies.get_dict()

def get_bets(cookies):
    import requests

    print("cookies: ", cookies)

    headers = {
        'authority': 'cf-mt-auth-api.kambicdn.com',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9',
        'authorization': 'Bearer c226ae74-9b7a-45cd-a127-ba991b32da60',
        'origin': 'https://www.leovegas.it',
        'referer': 'https://www.leovegas.it/',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    # get now date in 2023-10-27T22:00:00.000Z format
    now = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.000Z")

    response = requests.get(
        'https://cf-mt-auth-api.kambicdn.com/player/api/v2019/leoit/coupon/history.json?lang=it_IT&market=IT&toDate='+now,
        headers=headers, cookies=cookies
    )

    print(response.status_code)
    print(response.json())

    with open("cookies_Leovegas.JSON", "w") as f:
        json.dump(cookies, f)

    simplified_data = []

    for coupon in response.json()['historyCoupons']:
        # this 2023-10-21T18:45:00Z to 2023-10-21 18:45:00
        # eliminate last part of 2023-10-24 10.11.09.781 to 2023-10-24 10.11.09

        coupon['placedDate'] = coupon['placedDate'].replace('T', ' ').replace('Z', '').replace(':', '.')[:19]
        coupon['events'][0]['eventStartDate'] = coupon['events'][0]['eventStartDate'].replace('T', ' ').replace('Z',
                                                                                                                '').replace(
            ':', '.')

        simplified_coupon = {
            'startDate': coupon['placedDate'],  # Start date
            'endDate': coupon['events'][0]['eventStartDate'],  # End date from the first event
        }

        for bet in coupon['bets']:
            simplified_coupon['stake'] = bet['stake'] / 1000
            simplified_coupon['return'] = bet['payout'] / 1000
            simplified_coupon['bookmaker'] = "LeoVegas"

            if bet['betStatus'] == 'WON':
                simplified_coupon['result'] = 'WIN'
            elif bet['betStatus'] == 'LOST':
                simplified_coupon['result'] = 'LOSS'
            else:
                simplified_coupon['result'] = 'PENDING'

        simplified_data.append(simplified_coupon)


    return simplified_data


def main():
    # get cookies from William Hill Cookies file
    with open("cookies_Leovegas.JSON", "r") as f:
        cookies = json.load(f)

    try:
        get_bets(cookies)
    except Exception as e:
        print("token expired")
        cookies = get_token()
        get_bets(cookies)
        # update cookies file
        with open("cookies_Leovegas.JSON", "w") as f:
            json.dump(cookies, f)