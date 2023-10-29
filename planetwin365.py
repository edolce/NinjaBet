import datetime
import json

import requests

def get_cookies():

    cookies = {
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'srv_id=909246bca5e4bb0f38fbec3c5941445b; ASP.NET_SessionId=2wpjlnoa5vex51c2cuq42yao; ISBets_CurrentCulture=1; bm_sz=A11948DB8D99D0CD2FABB6AC3D1E1CEB~YAAQFGV7XKfjaGqLAQAAcM9PbRVhdl5X+RzOfrtz2xfusUrmXbWwxQLHdexr2tv2yuJa4bmLEX4si8quy9jhOmczGbqcEH661G/R6Bd5OFw7Y9sHQlpOPK/7XMosHp0m63mKonKhlN2Yny839R+sjGoyC6YJPoQaQgZgAcnWfRQx1X4loqRqb7wM7FiMl/k+fyyO7DqTh+HPoVazBuNjOOeEVErNBMzq3/13A5v2q+MW/nBA1GRwk5rpJ/V5yUGVwEm0LkpXLT6wlZPZhoVCddWga4jRqUmi+TtJANk/CSPPHn7vOgxZ4Q==~4405317~3163703; _gid=GA1.2.635996710.1698346030; _clck=1h65hde|2|fg6|0|1394; bm_mi=AD5DB4D241EFE06DA7F92AEEAD4D6144~YAAQNmV7XB9SE2uLAQAACddPbRUHmo2Di3oAhcvirO+lmteTEsjZE1slSsgqpbVqGJGRsfaGAI9iAC0jBurBsGU12ZlnJDjKa4TEa3yc9E3aJg1r2Tz0dsSm942EmnKsFQLFminX69eWazkYS/c817Mtp1rC45IUK89xwvV8lOV/t8Nb0UVeImza30W7D83L1dDlAh0Uam6xasL1zKxxUwzwt1GufndPwtihr99n+tQPPPxJAbn6Ude9uVUqxHwO+oFhy4ZBKWnRyS0HqS1xL/ByHYPlmmxQ8EgeCloA1mxkX+EOl40klBMmT0yg+7bqwSMAASeU88mvU4rYDDy5PkXR89TIBKHXVg==~1; ak_bmsc=D48C88BA440BECBC55C134083D59FEE9~000000000000000000000000000000~YAAQNmV7XE9SE2uLAQAAPtlPbRU6Vv/eP8zVWvMwvX3YNDEtWC4sFxN4tTiTfIHZMtLYq2AmqyqsWWG8SBf57cvMYHqbn2PluEEM2b23h35yG2+FZmjCEfn8XZ2z6sfdttwO344+jz4dBu5U5/jIzwUMY69O3Ln6tZ2I3/cTWnevqLE4Q5kmu/hpaLsrNllor5wD/B9i8b4wOA03nsYn+f6qzDcDJ29TEJpC4Kaz2ZbsxqHWy8GaeEFOU//Fp0PaFSDYf/izLrtdn94te78vtXave/hNPLUMPz/+KNhMobrEp5jXPbKsGaa/EihoFKrrVnvhiFrRSHdDFJVuR+uTZ3EkUdJbSpjVXvsKw2dIo8Msk0OBWV6Lt+64FNxsSmOYCu3YphFKioGKSolrd4vOZG/4CJ10jQufWDL09myb2+j5vKp/J0V6/gF2aqrL/xcL8jDy+z1ljGzLNcjNW/pIZGmgoybs+26d2R3DxQZMxdVfyZ7ePHMee3bhUy7hPLm1qyrtpMRxg7ArM4B1HYWLGqbwqpUTGA==; ISBetsCookie=ISBetsCookie=1350914847DB6A1BED0EDB956019A0FCFDA6F279F1D502D8BB55C0DAC3BBC50CE17DCA3A654DE50C4C8752F7ED3901AB; _aui=4654852; _abck=97B9F38D16806A721DBE546A35704E17~0~YAAQNmV7XM1TE2uLAQAA9vNPbQqi608xfldPhYBIpV9NWVIHCybwFkVEweVjjeONdw+uJUvklTExAAUAMOXENtMJs/AM5TiDInDAwwDKPgK9tFro8hwfeH+uFqbGlxpuFd9pGnFZevnpzKzveKxBBR0i852QWezUjCetJItCMPFU1RoD8htd8oQS2IRO7H3JXDI+3YgLBAanRIoukbjd1/SRvTL46Q5dkGdKQRhPINKB9iuS6+pqxZxuYEOZc5wn5IUC2VKPL6CBNzEGXF+rc5NQDCb0S/lQziQY4q0J3hn5OyQ0SSVKJhQ9B+b+Ef7ntnWg4LBt2O5do001kI6dKEHlBwT1DxXDfLMw4nqOkeVyTi8oVl6ydqjwb5spn9WHG+UxQWX3cVCd9xYnakUe2+DlbbasvrxcbXpoMso=~-1~-1~-1; _dc_gtm_UA-63917352-18=1; _gat_UA-63917352-3=1; _arh=www.planetwin365.it; _ga=GA1.1.1876430970.1698346030; _clsk=cr2b1h|1698346440488|11|1|b.clarity.ms/collect; _ga_Z5VBXPPDZQ=GS1.2.1698346031.1.1.1698346440.30.0.0; _ga_CJVTPK2RHC=GS1.1.1698346030.1.1.1698346443.0.0.0; _ga_Q5WYE5HWYS=GS1.1.1698345701.4.1.1698346443.0.0.0',
        'Origin': 'https://www.planetwin365.it',
        'Referer': 'https://www.planetwin365.it/it/scommesse?LogoutGroupID=7',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'X-MicrosoftAjax': 'Delta=true',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'LogoutGroupID': '7',
    }

    data = 'h%24w%24SM=h%24w%24SiteHeader%24cLoginRedesign%24ctrlLogin%24pnlUpdateLogin%7Ch%24w%24SiteHeader%24cLoginRedesign%24ctrlLogin%24lnkBtnLogin&h%24w%24SiteHeader%24cLoginRedesign%24ctrlLogin%24hndLoggedURL=&h%24w%24SiteHeader%24cLoginRedesign%24ctrlLogin%24Username=polly71&h%24w%24SiteHeader%24cLoginRedesign%24ctrlLogin%24Password=Lucetta3&h%24w%24PC%24oddsSearch%24txtSearch=&h%24w%24PC%24cSport%24hidSportTime=1&h%24w%24PC%24ctl01%24txtVincita=&h%24w%24PC%24ctl01%24txtGiocata=&h%24w%24PC%24CouponCheck1%24txtCodiceCoupon=&h%24w%24PC%24cCoupon%24hidRiserva=0&h%24w%24PC%24cCoupon%24hidAttesa=0&h%24w%24PC%24cCoupon%24hidIsTemporaryCoupon=&h%24w%24PC%24cCoupon%24hidTipoCoupon=&h%24w%24PC%24cCoupon%24hidStatoCoupon=0&h%24w%24PC%24cCoupon%24hidQuotaTotaleDIMax=&h%24w%24PC%24cCoupon%24hidQuotaTotaleDIMin=&h%24w%24PC%24cCoupon%24hidQuotaTotale=&h%24w%24PC%24cCoupon%24hidIDQuote=&h%24w%24PC%24cCoupon%24hidModificatoQuote=1&h%24w%24PC%24cCoupon%24hidNumItemCoupon=0&h%24w%24PC%24cCoupon%24hidIDCoupon=&h%24w%24PC%24cCoupon%24hidERBCoupon=0&h%24w%24PC%24cCoupon%24hidERBLastStatoChangeId=0&h%24w%24PC%24cCoupon%24hidERBReCheck=1&h%24w%24PC%24cCoupon%24hidERBStato=&h%24w%24PC%24cCoupon%24hidCoddAnonimo=&h%24w%24PC%24cCoupon%24hidCouponObject=&h%24w%24PC%24cCoupon%24txtCouponCodiceAnonimo=&h%24w%24PC%24cCoupon%24txtIDQuota=&h%24w%24PC%24cCoupon%24txtSottoEventName=&h%24w%24PC%24cCoupon%24txtQuota=&h%24w%24PC%24cCoupon%24txtCodPubblicazione=&h%24w%24PC%24cCoupon%24txtIDEvento=&h%24w%24PC%24cCoupon%24txtEventName=&h%24w%24PC%24cCoupon%24txtIDSottoEvento=&h%24w%24PC%24cCoupon%24txtGiocabilita=&h%24w%24PC%24cCoupon%24txtTipoQuota=&h%24w%24PC%24cCoupon%24txtIDTipoEvento=&h%24w%24PC%24cCoupon%24txtIDTipoQuota=&h%24w%24PC%24cCoupon%24txtDataSottoEvento=&h%24w%24PC%24cCoupon%24txtQB=&h%24w%24PC%24cCoupon%24txtAddImporto=&h%24w%24PC%24cCoupon%24txtCouponCreationType=&h%24w%24PC%24cCoupon%24txtClasseQuotaParamInstance=&h%24w%24PC%24cCoupon%24txtListItem=&h%24w%24PC%24cCoupon%24txtIDCouponPrecompilato=&h%24w%24PC%24cCoupon%24txtImportoCouponPrecompilato=&h%24w%24TermsAndConditionsPopup%24hndShowTCs=false&__EVENTTARGET=h%24w%24SiteHeader%24cLoginRedesign%24ctrlLogin%24lnkBtnLogin&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUJMjUzNTk5OTE4DxYCHg9QYWdlUGVybWlzc2lvbnMFB2VuYWJsZWQWAmYPZBYCZg9kFgRmD2QWAgIDDxYCHgRocmVmBVF%2BL0FwcF9UaGVtZXMvUGxhbmV0V2luMzY1SVRWVS9qcXVlcnktZXUtY29va2llLWxhdy1wb3B1cC5jc3M%2Fdj02MzgzMTkxOTc0MjAwMDAwMDBkAgEPZBYMAgMPDxYCHgdWaXNpYmxlaGRkAgcPZBYEAgIPZBYEAgEPZBYCAgEPZBYCZg9kFgICAQ9kFgJmD2QWAgIDD2QWCGYPDxYCHgtOYXZpZ2F0ZVVybAUafi9Db250ZW50L05ld1VzZXJXaWRlLmFzcHhkZAIBDw8WAh8DBR4vQWNjb3VudC9QYXNzd29yZFJlY292ZXJ5LmFzcHhkZAILDw8WAh4LUG9zdEJhY2tVcmxlZGQCDA8PFgIfAmdkZAIDDw8WAh8CaGQWAmYPFgIeBVZhbHVlBQVmYWxzZWQCBQ9kFgJmDxYCHwJoZAIID2QWDgIBD2QWAmYPZBYCZg9kFgICAQ8PFgIfAmhkZAIED2QWAgIED2QWAmYPZBYKAgIPDxYCHwJoZGQCAw8WAh8CZ2QCCA8WAh8CZ2QCCQ8WAh8CZ2QCCw8WAh8CZ2QCBQ9kFgJmDxYCHgRUZXh0BQlMb3R0byBXaW5kAgsPZBYCAgMPZBYCZg9kFhJmDxYCHgVjbGFzcwUDVG9wFgQCAw8PFgIfAmhkZAIHDw8WAh8CaGRkAhMPDxYEHghDc3NDbGFzcwUGcG5sRXJiHgRfIVNCAgJkFgYCDQ9kFgJmD2QWAgIDDzwrABECARAWABYAFgAMFCsAAGQCDw9kFgJmD2QWAgIDDzwrABECARAWABYAFgAMFCsAAGQCFQ8WAh4Fc3R5bGUFDWRpc3BsYXk6bm9uZTtkAhYPD2QWAh4Hb25LZXlVcAVEdHJhcE5leHRCZXQoZXZlbnQsICdoX3dfUENfY0NvdXBvbl9idG5TY29BbmNvcmFBc3luYycpO3JldHVybiBmYWxzZTtkAhcPFgIfAmhkAhgPFgIfAmhkAhsPFgIfAmgWCGYPFgIeC18hSXRlbUNvdW50Av%2F%2F%2F%2F8PZAICD2QWAgIHDxBkZBYAZAIDD2QWBgIBD2QWAgIDD2QWAgICDxBkZBYAZAIDD2QWAgIEDxBkZBYAZAIFD2QWAgICD2QWAgICDxBkZBYAZAIJD2QWBAIDDw8WBB8IBRJidG5Db3Vwb24gZHggdGhyZWUfCQICZGQCBQ8PFgQfCAUSYnRuQ291cG9uIHN4IHRocmVlHwkCAmRkAhwPFgIfAmgWAgIDD2QWAgIBD2QWBAIIDxYCHgdvbmNsaWNrBeYCb3BlbkFuYWdyYWZpY2FQb3BVcCgnL0NvbnRyb2xzL1dlYlNpdGUvQW5hZ3JhZmljYVBvcFVwLmFzcHgnLCdoX3dfUENfY0NvdXBvbl9jdHJsQW5hZ3JhZmljYVNlbGVjdF90eHRJREFuYWdyYWZpY2EnLCdoX3dfUENfY0NvdXBvbl9jdHJsQW5hZ3JhZmljYVNlbGVjdF90eHRBbmFncmFmaWNhJywnaF93X1BDX2NDb3Vwb25fY3RybEFuYWdyYWZpY2FTZWxlY3RfaGlkSURBbmFncmFmaWNhJywnaF93X1BDX2NDb3Vwb25fY3RybEFuYWdyYWZpY2FTZWxlY3RfaGlkQW5hZ3JhZmljYUNvZ25vbWUnLCdoX3dfUENfY0NvdXBvbl9jdHJsQW5hZ3JhZmljYVNlbGVjdF9oaWRBbmFncmFmaWNhTm9tZScsJycsJycsJycsJzEnKTt2b2lkKDApO2QCCQ8WAh8NBVBzdGFtcGFBbmFncmFmaWNhKCcvQWNjb3VudC9QcmludFBlcnNvbmFsRGV0YWlscy5hc3B4JywgJy0xJywgJzEnLCAnLTEnKTt2b2lkKDApO2QCHQ8WAh8CaBYEAgIPD2QWAh8LBT90cmFwTmV4dEJldChldmVudCwgJ2hfd19QQ19jQ291cG9uX2J0blNjb0FuY29yYScpO3JldHVybiBmYWxzZTtkAgMPD2QWAh8LBT90cmFwTmV4dEJldChldmVudCwgJ2hfd19QQ19jQ291cG9uX2J0blNjb0FuY29yYScpO3JldHVybiBmYWxzZTtkAjcPFgIfAmhkAgwPZBYGAgIPZBYCZg9kFgICAQ8PFgIfAmhkZAIFDw9kDxAWAWYWARYCHg5QYXJhbWV0ZXJWYWx1ZWYWAQIGZGQCBg8PZA8QFgFmFgEWAh8OZhYBAgZkZAIODw8WAh8CaGRkAhAPDxYCHwJoZGQCDA8PFgIfAmhkZAITDw8WAh8CaGRkAhQPDxYCHwJoZGQYAgUlaCR3JFBDJGNDb3Vwb24kZ3ZRdW90YU1vZGlmaWNhUmlzZXJ2YQ9nZAUbaCR3JFBDJGNDb3Vwb24kZ3ZEZXR0UmZpdXRvD2dkAyIk5FDWXwRUHzWesPKNZ4TepbY%3D&__VIEWSTATEGENERATOR=15C4A0A3&__EVENTVALIDATION=%2FwEdAEed%2Bdb9djNZTMpCTFKh6Lb7LAxdjiS30d7FDv7DzDZdW4esfN9wyVS1p3IlKtUQbit%2FL%2BMfad%2B7S753G2tkDFaI0bG3wxXjYI2zncXdxmrDdoU%2BvMggX6v%2FsFNrOQZHtdKZccnUfRo2DILUJjUJ9Bi8bGAKDs5hDQN0S9Qm4ZEU0fzPYWtSK5%2Br8HhULIMj7Riy0K9K7zs2n6CYQJjr0rBNdz67BPa1vPLmae%2BeLvU9t4QxMsZuMqYt%2BEQxLnCg0P%2Fl%2BVMKGAbIsBZMMQZgj8e2c%2BtJI9TU7Rx4BluEPQHHsG0aO1hXXbEgNFix0TTZYlmeS1f5DLm27Lo99VtRsMp5wrHoh7ZYh1TGbBVYleax2s7CtCMIB2oII8TXVua8k%2Byo6ROieUJRCC0sKgKlqXI1rWS1RWOOiERl4X3FxCBt7igAOzNhfODV6CX4pZXPE7BMtm%2FpIZcSPjNeETyWve7SN4MH7iYlC5mnePoj3wO5%2BvRBjB7%2BgARQREVN3iBgh%2BnFMl8UFpzxH0u%2FoeNLL2jgTGjzdP16kYPK5nrzmNU50VZJc7wdDYBHuKBZLd4CrPPNVFQUVUzNCwsA3qqS4O2PTNb2lPqbahI%2Fc1wHedeH5f7sQA2vMqzI5rwQK8wpgYG4idierwzUWQbxsp5hs%2BoJScXu4cCn3OyoOiN4c0%2FCRZW6iEyltr8dgwPs1nDE%2BAQC5FuzSjsI%2F8oVAM1LyXvLJPiqZu%2BiUFkspybocPJo%2BqUKi9pmRH0qAkIqwoSyos%2B%2FMLcUVD6J6q4sBIcJzijFNcetQZtZDJT5Rxbw8Y0FjSnJ414dWc6hgtCrxD9nQYmU7KiaRwagORrzckq5xVfDw0ohUNu4a9XLvDfIk44cWwZqOK0rVthI1hdAJQnxW5jvnp%2F7hzjrucrvWUCEjNTVyoQ8%2BwL%2BxnEGJZLHxV15TwUhPimF5xNYlQSKhOs7YwjETcrEcJJYA1vBEnaREZWccuwi6Lspg7KBcmurm6YFyhencaMW35w6ZsCxBCQ%2Byqo0xq0zJowGISTpYvJ54elD6jJh704Bu7QRVPQkHGdQa7vsG3mAwsr9D5LUwQdHKbZlhUx0NkdHniDhHlSg0raT4uvOODzXPxdFlMYr5MJldl1c5G%2B%2B0FujIEd7px21t02WKKuql4Gs3I6TfBp%2FewOs0%2FFzNIAhDlG3eNtm%2B7OxBQZ8TvMHujFhI9uNHipns3xTkUNklkGeTi0WYiDjPNs%2Br1zcjSPtngaiySqqbvp8QTEO4OMgrDLhhdnsKBbad001%2FXN3ybHKF5NFXq8dVmLEB3DWpqwHgEzzsqz0LtY5djueeWkI%2BxS85bw40OEiymrIdqpZuy2%2BY4omirD46ChKUpCM%2BvhuqVAPFG0WEtTTLKhwjXqhHroelDXEogHZY9GezgTr8pp9wUSb7ACMPvDd3hvMOYEdGi38HXyI69l%2B9xfR2rEC8tWUpNHEWffq%2F4h04mSz6gtSyLR5%2FMVmcsdJYv0JZJ6ghfaNcX1c1S3YAxDqGVCzxkGCTTz6WQho4QEDR0iW&__ASYNCPOST=true&'

    response = requests.post('https://www.planetwin365.it/it/scommesse', params=params, cookies=cookies, headers=headers, data=data)

    return response

#
#
#
#
#
# import requests
#
# cookies = response.cookies.get_dict()


def get_bets(response=None):
    if response is None:
        # get cookies from file
        with open('cookies.json', 'r') as f:
            cookies = json.load(f)
    else:
        cookies = {
            'ASP.NET_SessionId': response.cookies.get_dict()["ASP.NET_SessionId"],
            'ISBetsForm': response.cookies.get_dict()["ISBetsForm"]
        }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'srv_id=909246bca5e4bb0f38fbec3c5941445b; ASP.NET_SessionId=2wpjlnoa5vex51c2cuq42yao; ISBets_CurrentCulture=1; bm_sz=A11948DB8D99D0CD2FABB6AC3D1E1CEB~YAAQFGV7XKfjaGqLAQAAcM9PbRVhdl5X+RzOfrtz2xfusUrmXbWwxQLHdexr2tv2yuJa4bmLEX4si8quy9jhOmczGbqcEH661G/R6Bd5OFw7Y9sHQlpOPK/7XMosHp0m63mKonKhlN2Yny839R+sjGoyC6YJPoQaQgZgAcnWfRQx1X4loqRqb7wM7FiMl/k+fyyO7DqTh+HPoVazBuNjOOeEVErNBMzq3/13A5v2q+MW/nBA1GRwk5rpJ/V5yUGVwEm0LkpXLT6wlZPZhoVCddWga4jRqUmi+TtJANk/CSPPHn7vOgxZ4Q==~4405317~3163703; _gid=GA1.2.635996710.1698346030; _clck=1h65hde|2|fg6|0|1394; bm_mi=AD5DB4D241EFE06DA7F92AEEAD4D6144~YAAQNmV7XB9SE2uLAQAACddPbRUHmo2Di3oAhcvirO+lmteTEsjZE1slSsgqpbVqGJGRsfaGAI9iAC0jBurBsGU12ZlnJDjKa4TEa3yc9E3aJg1r2Tz0dsSm942EmnKsFQLFminX69eWazkYS/c817Mtp1rC45IUK89xwvV8lOV/t8Nb0UVeImza30W7D83L1dDlAh0Uam6xasL1zKxxUwzwt1GufndPwtihr99n+tQPPPxJAbn6Ude9uVUqxHwO+oFhy4ZBKWnRyS0HqS1xL/ByHYPlmmxQ8EgeCloA1mxkX+EOl40klBMmT0yg+7bqwSMAASeU88mvU4rYDDy5PkXR89TIBKHXVg==~1; ak_bmsc=D48C88BA440BECBC55C134083D59FEE9~000000000000000000000000000000~YAAQNmV7XE9SE2uLAQAAPtlPbRU6Vv/eP8zVWvMwvX3YNDEtWC4sFxN4tTiTfIHZMtLYq2AmqyqsWWG8SBf57cvMYHqbn2PluEEM2b23h35yG2+FZmjCEfn8XZ2z6sfdttwO344+jz4dBu5U5/jIzwUMY69O3Ln6tZ2I3/cTWnevqLE4Q5kmu/hpaLsrNllor5wD/B9i8b4wOA03nsYn+f6qzDcDJ29TEJpC4Kaz2ZbsxqHWy8GaeEFOU//Fp0PaFSDYf/izLrtdn94te78vtXave/hNPLUMPz/+KNhMobrEp5jXPbKsGaa/EihoFKrrVnvhiFrRSHdDFJVuR+uTZ3EkUdJbSpjVXvsKw2dIo8Msk0OBWV6Lt+64FNxsSmOYCu3YphFKioGKSolrd4vOZG/4CJ10jQufWDL09myb2+j5vKp/J0V6/gF2aqrL/xcL8jDy+z1ljGzLNcjNW/pIZGmgoybs+26d2R3DxQZMxdVfyZ7ePHMee3bhUy7hPLm1qyrtpMRxg7ArM4B1HYWLGqbwqpUTGA==; _aui=4654852; _abck=97B9F38D16806A721DBE546A35704E17~0~YAAQNmV7XM1TE2uLAQAA9vNPbQqi608xfldPhYBIpV9NWVIHCybwFkVEweVjjeONdw+uJUvklTExAAUAMOXENtMJs/AM5TiDInDAwwDKPgK9tFro8hwfeH+uFqbGlxpuFd9pGnFZevnpzKzveKxBBR0i852QWezUjCetJItCMPFU1RoD8htd8oQS2IRO7H3JXDI+3YgLBAanRIoukbjd1/SRvTL46Q5dkGdKQRhPINKB9iuS6+pqxZxuYEOZc5wn5IUC2VKPL6CBNzEGXF+rc5NQDCb0S/lQziQY4q0J3hn5OyQ0SSVKJhQ9B+b+Ef7ntnWg4LBt2O5do001kI6dKEHlBwT1DxXDfLMw4nqOkeVyTi8oVl6ydqjwb5spn9WHG+UxQWX3cVCd9xYnakUe2+DlbbasvrxcbXpoMso=~-1~-1~-1; _arh=www.planetwin365.it; ISBetsCookie=ISBetsCookie=1350914847DB6A1BED0EDB956019A0FCE200AC9048BA2C25A36F3F704F13D17BE17DCA3A654DE50C4C8752F7ED3901AB; mess=0; fginfo=1; _ga=GA1.2.1876430970.1698346030; _ga_Z5VBXPPDZQ=GS1.2.1698346031.1.1.1698346625.60.0.0; _clsk=cr2b1h|1698346625023|13|1|b.clarity.ms/collect; ISBetsForm=ED7270FE9EA4AFE464FDBEF67E75B925079CF988E62F9DFF54A44589341FD51BBC0DE92C6BD401AA53580201D3D26443D0D8B5793B7C265D406425241A83498ABAB878A11DD08AECB9E2A69BEC89CA4E7A6C8F4328786F4A833B99210853AAE4EE524DAC83132CFD43C13EA39C9A62D8EE032355; _ga_CJVTPK2RHC=GS1.1.1698346030.1.1.1698347883.0.0.0; _ga_Q5WYE5HWYS=GS1.1.1698345701.4.1.1698347883.0.0.0',
        'Origin': 'https://www.planetwin365.it',
        'Referer': 'https://www.planetwin365.it/it/sport/betlist',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    # get today's date in the format dd/mm/yyyy
    today = datetime.datetime.now()
    today = today.strftime("%d/%m/%Y")

    # get 59 days from today's date in the past format dd/mm/yyyy
    past = datetime.datetime.now() - datetime.timedelta(days=59)
    past = past.strftime("%d/%m/%Y")


    data = {
        'ac$w$SiteHeader$cLoginRedesign$hndShowTCs': 'false',
        'ac$w$SiteHeader$cLoginRedesign$hndNotificationDocument': 'false',
        'ac$w$PC$PC$ddlFiltoData': '1',
        'ac$w$PC$PC$cpopDal$txtDate': past,
        'ac$w$PC$PC$cpopAl$txtDate': today,
        'ac$w$PC$PC$txtCodiceCoupon': '',
        'ac$w$PC$PC$ddlEsito': '0',
        'ac$w$PC$PC$ddlPageSize': '15',
        'ac$w$PC$PC$btnAvanti': 'Avanti',
        'ac$w$PC$PC$ImportoTotPagina': '250,00',
        'ac$w$PC$PC$VincitaTotPagina': '0,00',
        'ac$w$TermsAndConditionsPopup$hndShowTCs': 'false',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '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',
        '__VIEWSTATEGENERATOR': 'DBD931C2',
        '__VIEWSTATEENCRYPTED': '',
        '__EVENTVALIDATION': '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',
    }

    response = requests.post('https://www.planetwin365.it/it/sport/betlist', cookies=cookies, headers=headers, data=data)

    from bs4 import BeautifulSoup

    beautifulSoup = BeautifulSoup(response.text, 'html.parser')

    # search tbody tag
    tbody = beautifulSoup.find('table', class_='dgStyle')
    feedback = []
    print(tbody)

    import util

    # all interno di ogni tr
    for tr in tbody.find_all('tr'):
        data = tr.text.strip()
        data = data.split('\n')
        for i in range(len(data)):
            data[i] = data[i].strip()
        try:
            parsed_data = util.sheet_bet('planetwin365', data[2], data[9], data[12], data[13], data[6], data[8])

            feedback.append(parsed_data)
        except:
            pass
        # print

    #update cookies in file
    with open('cookies.json', 'w') as outfile:
        json.dump(cookies, outfile)
    print(feedback)
    return feedback

def main():
    try:
        return get_bets()
    except Exception as e:
        return get_bets(get_cookies())