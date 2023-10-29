import datetime
import json
import time

import requests


def get_login_cookie():
    print("\n[LEOVEGAS] - Getting Login Cookie:")
    print("-----------------------------------")

    cookies = {
        'leonrpid': '3758383',
        'leonrbid': '13309',
        'nlbi_1705993': '02OWI0hI0y0NelKA9tXEVgAAAAAdUC0nrFcQV2s2P1e97cPp',
        'leobtag': '100664721_4AA2E15CED8D4C4AAFF4B91556F42F8E',
        'leonrmeta': '[{"value":"sportsbook","key":"lobby"},{"value":"sports","key":"verticalSort"}]',
        '__zlcmid': '1IRmDG58tfR3RGC',
        'incap_ses_416_1705993': '1GWNZ5UX8zkF3be4fO7FBcJXNWUAAAAAYlOSYMFuo9o0CafmIfPNdQ==',
        'incap_ses_475_1705993': 'fudYVPxR8wF4OdfGHouXBrwFNmUAAAAAwL6tucyZMx9TPN1li7/hZw==',
        'incap_ses_890_1705993': 'y9PiRsVZiV295wNLWetZDNo0NmUAAAAA0RXWEdng0UomrvHRuQHO/A==',
        'incap_ses_1576_1705993': 'yuT1dNXctFZiF3jQIRTfFQOrOGUAAAAA4nSTcVXZAtf345slWc61Qg==',
        'leo-essentials': '%7B%22cid%22%3A%228210ff42-d3fe-4f4a-b942-279a5e0f57e7%22%2C%22rc%22%3Atrue%7D',
        'data': 'eb44b6014dc8d1294112dd4e337438bf',
        'incap_ses_1573_1705993': 'mZRVBiWKJHAupt7mpWvUFXoiPmUAAAAAh1DtbljaQEaBXVQFJxGm7A==',
        'incap_ses_237_1705993': 'FQWpZhyK6k2HLX0ZJf9JAxYoPmUAAAAA5/E4IbH95wPLYBWlZtFahg==',
        'incap_ses_1523_1705993': 'ceIrENY0IjAi0yXH/sgiFakrPmUAAAAArLhauW22Pm/LQy8h7JPCQQ==',
        'incap_ses_578_1705993': 'AUUjRE7EhWtjjXsnjHkFCGFFPmUAAAAAHP5omnT2fmIQb9FEOQZrSg==',
        'visid_incap_1705993': 'DdRVILQJTaWpIl3IdqFMPg1T3mQAAAAAQ0IPAAAAAACAHfmvAV0saEwMDvmPyRIOXt/wTIVADx8Z',
        '_dd_s': 'rum=1&id=00858755-5ad3-4faf-91bf-a831b92165bf&created=1698588126338&expire=1698589031505',
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
        'x-request-id': 'c9b3976c-e6f8-4e62-98d8-7470b8c8fedb',
    }
    json_data = {
        'operationName': 'LoginWithPasswordMutation',
        'query': 'mutation LoginWithPasswordMutation(\n  $input: LoginWithPasswordInput!\n) {\n  loginWithPassword(input: $input) {\n    viewer {\n      authenticated\n      locale {\n        string\n      }\n      unixTimestamp\n      user {\n        userId\n        clientIP\n        license {\n          name\n        }\n        balance {\n          amount\n          fetchedAt\n          totalBonusCasino\n          pendingWithdrawal {\n            amount\n          }\n        }\n        country {\n          code\n          tncVersion\n          id\n        }\n        currency\n        details {\n          nickname\n          firstName\n          lastName\n          gender\n          dateOfBirth\n          mobileNumber\n          mobileNumberPrefix\n          address {\n            city\n            zip\n          }\n        }\n        stats {\n          latestLogin\n          created\n          isPasswordExpired\n        }\n        pendingDocumentationRequests {\n          verifiedUntil\n        }\n        acceptedTnC\n        status\n        thirdPartyAccounts {\n          provider\n        }\n        id\n      }\n      id\n    }\n  }\n}\n',
        'variables': {
            'input': {
                'password': 'Lucetta3#',
                'username': 'piumarg@yahoo.it',
                'blackbox': 'Web;6ec3a635-fdc6-4c2f-aaa8-594743a629db;CfLLSdh6ZJwq/hVtkA8Flw==;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',
            },
        },
    }

    response = requests.post('https://www.leovegas.it/api?relay', headers=headers, json=json_data,cookies=cookies)

    from twocaptcha import TwoCaptcha

    solver = TwoCaptcha("8e4d3a745d75dc4a4461b1f7d891c636")
    if "_Incapsula_Resource" in response.text:
        print("Recaptcha detected")
        try:
            result = solver.recaptcha(
                sitekey='6Ld38BkUAAAAAPATwit3FXvga1PI6iVTb6zgXw62',
                url='https://www.leovegas.it',
                version='v2')

            print("[LEOVEGAS] - Result of recaptcha bypass: ", result)

            cts = response.text.split("cts=")[1].split("&")[0]

            print(cts)

            response = requests.post('https://www.leovegas.it/_Incapsula_Resource?SWCGHOEL=v2&cts=' + cts,
                                     headers=headers, json={
                    "g-recaptcha-response": result['code']
                })

            print("CTS-resolver response text: ", response.text)

            response = requests.post('https://www.leovegas.it/api?relay', headers=headers,
                                     json=json_data,cookies=cookies)

        except Exception as e:
            print(e)

    print("Cookie request status: ", response.status_code)
    try:
        print("Cookie request json: ", response.json())
    except:
        print("No json response")
        print("Cookie request text: ", response.text)

    print("Cookie request cookies: ", response.cookies.get_dict())


    # merge cookies
    cookies.update(response.cookies.get_dict())

    print("\nSaving in file...")
    with open("cookies_Leovegas.JSON", "w") as f:
        json.dump(cookies, f)

    print("--------------------")


    return cookies


def get_bets(cookies):
    import requests

    print("\n[LEOVEGAS] - Getting sport token:")
    print("--------------------")

    headers = {
        'authority': 'www.leovegas.it',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'visid_incap_1705993=KAlAhUV5TMS9GzUMov4vbVANOmUAAAAAQUIPAAAAAABJ1W8ww/BIQl6HLL/W77tM; nlbi_1705993=zlWUe2WuvjrzrkQw9tXEVgAAAABs/To2NzHMqvoAzvWWX8vS; incap_ses_477_1705993=UcK/cLRtcm7COJtW1qaeBlANOmUAAAAATxH1vJZlPjd5qtK9rbLeYQ==; FPID=FPID2.2.8mypsk%2FZEzTjeqldQQufzxa59glgEdC1Y7omqHbaav4%3D.1698303318; _gcl_au=1.1.416797156.1698303318; FPAU=1.2.1204045000.1698303317; data=5f71c28f511989bbfc16e012f96c37af; leo-essentials=%7B%22cid%22%3A%2202c48cb8-0d1c-4a3c-b390-4bdc49dc3c2a%22%2C%22rc%22%3Atrue%7D; _ga=GA1.2.336119500.1698303318; FPLC=xcdbUJh2saSKX2XWoYxeFtcHzIZiNoKKConp7trd1bgNchkUYPzNiibHLqlbF7W%2B0GA5YyzRlRJGAFPVSgx48u5mUuNDLsKOEWGbxai9TLZ%2B5%2F1KrGjE2KfWtwyEug%3D%3D; leo-sid=s%3Alags-jKOu96IUCnSLN4anPIGN5zY-EBpJ31rB.Zwh%2BWgqa8T8WK%2BpPGb7FxDJb%2FzQjCXcHGpFzhCu%2Bf4I; _gat_leo=1; _gat_sportsbookv3=1; leo_previous_page=https://www.leovegas.it/it-it/login; _ga_B4STQPNQJ2=GS1.1.1698404735.2.1.1698404897.0.0.0; _dd_s=rum=1&id=94d8b357-bbfe-4913-9e5d-213a86067d49&created=1698404735508&expire=1698405801845',
        'origin': 'https://www.leovegas.it',
        'referer': 'https://www.leovegas.it/it-it/scommesse-sportive',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-leo-locale': 'it-it',
        'x-request-id': '34f767a0-ef61-4b4e-8419-0056e8458613',
    }
    json_data = {
        'operationName': 'SportsAuthTokenMutation',
        'query': 'mutation SportsAuthTokenMutation {\n  sportsAuthToken\n}\n',
        'variables': {},
    }

    response = requests.post('https://www.leovegas.it/api?relay', cookies=cookies, headers=headers, json=json_data)

    from twocaptcha import TwoCaptcha

    solver = TwoCaptcha("8e4d3a745d75dc4a4461b1f7d891c636")
    if "_Incapsula_Resource" in response.text:
        print("Recaptcha detected")
        try:
            result = solver.recaptcha(
                sitekey='6Ld38BkUAAAAAPATwit3FXvga1PI6iVTb6zgXw62',
                url='https://www.leovegas.it',
                version='v2')

            print("[LEOVEGAS] - Result of recaptcha bypass: ", result)

            cts = response.text.split("cts=")[1].split("&")[0]

            response = requests.post('https://www.leovegas.it/_Incapsula_Resource?SWCGHOEL=v2&cts=' + cts,
                                     cookies=cookies, headers=headers, json={
                    "g-recaptcha-response": result['code']
                })

            print("CTS-resolver response text: ", response.text)

            response = requests.post('https://www.leovegas.it/api?relay', cookies=cookies, headers=headers,
                                     json=json_data)



        except Exception as e:
            print(e)

    print("Sport-Token response status: ", response.status_code)
    print("Sport-Token response text: ", response.text)
    print("Sport-Token response json: ", response.json())
    print("Sport-Token response cookies: ", response.cookies.get_dict())

    print("----------------------")

    sportsAuthToken = response.json()['data']['sportsAuthToken']

    print("\n[LEOVEGAS] - Get bet list token:")
    print("----------------------")

    headers = {
        'authority': 'cf-mt-auth-api.kambicdn.com',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.leovegas.it',
        'referer': 'https://www.leovegas.it/',
        'sec-ch-ua': '"Opera";v="103", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0',
    }

    json_data = {
        'ticket': sportsAuthToken,
        'punterId': '300913183',
        'channel': 'MOBILE',
        'market': 'IT',
    }

    response = requests.post(
        'https://cf-mt-auth-api.kambicdn.com/player/api/v2019/leoit/punter/login.json',
        headers=headers,
        json=json_data,
    )

    print("GetTokenBet status: ", response.status_code)
    print("GetTokenBet text: ", response.text)
    print("GetTokenBet json: ", response.json())
    print("GetTokenBet cookies: ", response.cookies.get_dict())
    print("----------------------")

    print("\n[LEOVEGAS] - Get bet list:")
    print("----------------------")

    headers = {
        'authority': 'cf-mt-auth-api.kambicdn.com',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9',
        'authorization': 'Bearer ' + response.json()['token'],
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
        'https://cf-mt-auth-api.kambicdn.com/player/api/v2019/leoit/coupon/history.json?lang=it_IT&market=IT&toDate=' + now,
        headers=headers, cookies=cookies
    )

    print("GetBetList status: ", response.status_code)
    print("GetBetList text: ", response.text)
    print("GetBetList json: ", response.json())
    print("GetBetList cookies: ", response.cookies.get_dict())
    print("----------------------")

    import util
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

        simplified_data.append(
            util.sheet_bet(
                "LeoVegas",
                "SINGOLA",
                simplified_coupon['stake'],
                simplified_coupon['return'],
                simplified_coupon['result'],
                simplified_coupon['startDate'],
                simplified_coupon['endDate']
            )
        )

    with open("cookies_Leovegas.JSON", "w") as f:
        json.dump(cookies, f)

    print("\n[LEOVEGAS] - Simplified data: ", simplified_data)
    print("\n\n")

    return simplified_data


def main():
    # get cookies from William Hill Cookies file
    with open("cookies_Leovegas.JSON", "r") as f:
        cookies = json.load(f)

    try:
        return get_bets(cookies)
    except Exception as e:
        print("Cookie Expired, getting new cookie...")
        cookies = get_login_cookie()
        return get_bets(cookies)
        # update cookies file


if __name__ == '__main__':
    main()
