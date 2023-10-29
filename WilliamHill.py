import json

import requests

def get_sc_session():
    import requests
    headers = {
        'authority': 'auth.williamhill.it',
        'accept': 'application/json',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'CASUN=Polly7103; TS0171ee0a=01c57796b19073593e518d979d6c15849a2c07ae858f4f001b11108f39a951a34606cceac676a0c83e217d19492b260eaa26887e4a; CASFLA=0; KeepMeLoggedIn=false; TS01c59c0f=011d05892377e2c075d0adbedab558e948b8aced277456a58737fd27974b9401059695416998345379916d3acc345d7515e615909f; ddl_landing_document_location=https://www.williamhill.it/; trk_jsoncookie=%7B%22serveGroup%22%3A32.457872162141555%7D; GoogleClickId=undefined; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=it-IT; CountryCodeCookie=IT; cust_lang=it; is_cas=Y; sitePreference=DESKTOP; landingURL=https%3A%2F%2Fsports.williamhill.it%2Fbetting%2Fit-it; trk_uid=05594MN; lastSiteVisited=https://sports.williamhill.it; xsys_balance=; banner_click=NA,NA,NA,NA,admap:d_direct%3Bsource:%3Bzone:%3Bchannel:; banner_domainclick=NA,NA,NA,NA,admap:d_direct%3Bsource:%3Bzone:%3Bchannel:; click_info=pid=0&bid=0; vars_info=; source_NR=NR; cust_auth=6d5e5b2b7c04a6c624a89bd018e5f7a26d046a3bdee54f12c63c96ab9b747cefadf9d60af968ca26d5; CONSENTMGR=consent:true%7Cts:1698305261815%7Cid:018b51f27ec6001fd2cca4c3d4750506f001b06700fb8; _rdt_uuid=1698305261937.5d40495f-53f2-43ae-8fb4-c76c0c60d399; _cs_ex=1658816546; _cs_c=1; _gid=GA1.2.652001140.1698308282; aws_bts=true; hide_header=0; tealium_data=%7B%22effortAttempt%22%3A1%2C%22landingDocumentLocation%22%3A%22https%3A//sports.williamhill.it/bet_ita/it%3Faction%3DDoHistory%26start_day%3D1%26start_month%3D1%26start_year%3D2007%26end_day%3D8%26end_month%3D6%26end_year%3D2018%26txn_type%3DBET_OPEN%26stateTime%3DSELECTION%26_start_day%3D1%26_start_month%3D1%26_start_year%3D2007%26resultsOnly%3D1%26source%3DCP%22%2C%22isExistingPaymentMethodFlag%22%3Anull%2C%22isFirstDeposit%22%3Anull%2C%22isRegistrationDeposit%22%3Afalse%2C%22depStartEventTriggered%22%3Afalse%2C%22loginStatus%22%3A%22Logged%20In%22%7D; wh_device={"is_native":"false","device_os":"desktop","os_version":"0","is_tablet":false}; CASLLD=2023-10-26T22:27:27; cust_prefs=it|DECIMAL|form|TYPE|PRICE|||1698352934-0|SB|0|0||0|it|1|TIME|TYPE|0|2|A|0||0|0||TYPE||-|0.00; TS0126ce9e=01ab52427b2f229667f79d75b6c0a68289cecb37740fb2a312889325d55978c4e5a782a36466a2894e6a9c2e5f3c84d9a341cb06ee; TS01f9a9d1=01975f9014c8ee65b37203eaf0d3d8207a6b511e2656709ccf18a2b115f17f72f894ba5cecad53bf659fecbb922b5cf2909963ebe2; OB_KEY=79897a7f116e49f58e66abb101613b03; cust_ssl_login_samesite=; CSRF_COOKIE=7cf14ce11b84f1d6a650; TS0192828e=0125ced71692c7844fb32343931db65334db56eb499bf0071e7f2139928382c80b7851871cfe0ae2e444ffcf6a419aaff8db58ae59; _cs_mk=0.8385365899027852_1698398160598; TS018bddb2=01c57796b19073593e518d979d6c15849a2c07ae858f4f001b11108f39a951a34606cceac676a0c83e217d19492b260eaa26887e4a; _gat_gtag_UA_136626402_3=1; _ga=GA1.2.31717655.1698308282; TS014de5c1=0184031e94dbf0bcdf94370630903ad009d4b1ded7cf514a01b4cdca64d70a4e2e4cc9f14c0bbf0e5cddd43196880a1ce8a4c39dfc; utag_main=v_id:018b51f27ec6001fd2cca4c3d4750506f001b06700fb8$_sn:8$_se:3$_ss:0$_st:1698399968165$dc_visit:8$ses_id:1698398159656%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session; _ga_Q5E35JEC8M=GS1.1.1698398161.6.1.1698398168.0.0.0',
        'origin': 'https://sports.williamhill.it',
        'referer': 'https://sports.williamhill.it/betting/it-it',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    response = requests.get('https://auth.williamhill.it/cas/v2/login', headers=headers)


    executionKey = response.json()["form_defaults"]["executionKey"]



    headers = {
        'authority': 'auth.williamhill.it',
        'accept': 'application/json',
        'accept-language': 'ql',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': 'CASUN=Polly7103; TS0171ee0a=01975f9014b47d22e5e47e68b7ad12722d639bad006bbba2dbe27288aecb569e4182d9dee991891d6f441e084876d44665768deb3b; CASFLA=0; KeepMeLoggedIn=false; TS01c59c0f=011d05892377e2c075d0adbedab558e948b8aced277456a58737fd27974b9401059695416998345379916d3acc345d7515e615909f; ddl_landing_document_location=https://www.williamhill.it/; trk_jsoncookie=%7B%22serveGroup%22%3A32.457872162141555%7D; GoogleClickId=undefined; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=it-IT; CountryCodeCookie=IT; cust_lang=it; is_cas=Y; sitePreference=DESKTOP; landingURL=https%3A%2F%2Fsports.williamhill.it%2Fbetting%2Fit-it; trk_uid=05594MN; lastSiteVisited=https://sports.williamhill.it; xsys_balance=; banner_click=NA,NA,NA,NA,admap:d_direct%3Bsource:%3Bzone:%3Bchannel:; banner_domainclick=NA,NA,NA,NA,admap:d_direct%3Bsource:%3Bzone:%3Bchannel:; click_info=pid=0&bid=0; vars_info=; source_NR=NR; cust_auth=6d5e5b2b7c04a6c624a89bd018e5f7a26d046a3bdee54f12c63c96ab9b747cefadf9d60af968ca26d5; CONSENTMGR=consent:true%7Cts:1698305261815%7Cid:018b51f27ec6001fd2cca4c3d4750506f001b06700fb8; _rdt_uuid=1698305261937.5d40495f-53f2-43ae-8fb4-c76c0c60d399; _cs_ex=1658816546; _cs_c=1; _gid=GA1.2.652001140.1698308282; aws_bts=true; hide_header=0; tealium_data=%7B%22effortAttempt%22%3A1%2C%22landingDocumentLocation%22%3A%22https%3A//sports.williamhill.it/bet_ita/it%3Faction%3DDoHistory%26start_day%3D1%26start_month%3D1%26start_year%3D2007%26end_day%3D8%26end_month%3D6%26end_year%3D2018%26txn_type%3DBET_OPEN%26stateTime%3DSELECTION%26_start_day%3D1%26_start_month%3D1%26_start_year%3D2007%26resultsOnly%3D1%26source%3DCP%22%2C%22isExistingPaymentMethodFlag%22%3Anull%2C%22isFirstDeposit%22%3Anull%2C%22isRegistrationDeposit%22%3Afalse%2C%22depStartEventTriggered%22%3Afalse%2C%22loginStatus%22%3A%22Logged%20In%22%7D; wh_device={"is_native":"false","device_os":"desktop","os_version":"0","is_tablet":false}; CASLLD=2023-10-26T22:27:27; cust_prefs=it|DECIMAL|form|TYPE|PRICE|||1698352934-0|SB|0|0||0|it|1|TIME|TYPE|0|2|A|0||0|0||TYPE||-|0.00; TS0126ce9e=01ab52427b2f229667f79d75b6c0a68289cecb37740fb2a312889325d55978c4e5a782a36466a2894e6a9c2e5f3c84d9a341cb06ee; TS01f9a9d1=01975f9014c8ee65b37203eaf0d3d8207a6b511e2656709ccf18a2b115f17f72f894ba5cecad53bf659fecbb922b5cf2909963ebe2; OB_KEY=79897a7f116e49f58e66abb101613b03; cust_ssl_login_samesite=; CSRF_COOKIE=7cf14ce11b84f1d6a650; TS0192828e=0125ced71692c7844fb32343931db65334db56eb499bf0071e7f2139928382c80b7851871cfe0ae2e444ffcf6a419aaff8db58ae59; _cs_mk=0.8385365899027852_1698398160598; _gat_gtag_UA_136626402_3=1; _ga=GA1.2.31717655.1698308282; TS014de5c1=0184031e94dbf0bcdf94370630903ad009d4b1ded7cf514a01b4cdca64d70a4e2e4cc9f14c0bbf0e5cddd43196880a1ce8a4c39dfc; utag_main=v_id:018b51f27ec6001fd2cca4c3d4750506f001b06700fb8$_sn:8$_se:3$_ss:0$_st:1698399968165$dc_visit:8$ses_id:1698398159656%3Bexp-session$_pn:1%3Bexp-session$dc_event:1%3Bexp-session; _ga_Q5E35JEC8M=GS1.1.1698398161.6.1.1698398168.0.0.0; TS018bddb2=01975f9014b47d22e5e47e68b7ad12722d639bad006bbba2dbe27288aecb569e4182d9dee991891d6f441e084876d44665768deb3b',
        'origin': 'https://sports.williamhill.it',
        'referer': 'https://sports.williamhill.it/betting/it-it',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    data = {
        'username': 'Polly7103',
        'password': 'Lucetta3',
        'rememberMe': 'false',
        'rememberUsername': 'true',
        '_rememberUsername': 'on',
        '_rememberMe': 'off',
        'lt': '1',
        'execution': executionKey,
        '_eventId': 'submit',
    }

    response = requests.post('https://auth.williamhill.it/cas/v2/login', headers=headers, data=data)

    cookies = response.cookies.get_dict()


    headers = {
        'authority': 'auth.williamhill.it',
        'accept': 'application/json',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'CASUN=Polly7103; TS0171ee0a=01c57796b1ce5e560a3acea5866f130071aba6c94847aef00e2c6a9de2dab8118bfe7121b86cfedb5bc910f183b076dd1bde9c3aa8; CASTGC=TGT-197125-fHVC0bXC35liaWNpP98AxTozd5gTpFsqP6UUnYPM1xMPBd0yvv9Yhos6-nsqGqaQ5zs-ip-100-76-144-101; CASTGC_CORS=TGT-197125-fHVC0bXC35liaWNpP98AxTozd5gTpFsqP6UUnYPM1xMPBd0yvv9Yhos6-nsqGqaQ5zs-ip-100-76-144-101; CASFLA=0; KeepMeLoggedIn=false; TS01c59c0f=01c57796b1ce5e560a3acea5866f130071aba6c94847aef00e2c6a9de2dab8118bfe7121b86cfedb5bc910f183b076dd1bde9c3aa8; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=it-IT; ddl_landing_document_location=https://sports.williamhill.it/betting/it-it; utag_main=_sn:1$_se:1$_ss:1$_st:1698401197199$ses_id:1698399397199%3Bexp-session$_pn:1%3Bexp-session; GoogleClickId=undefined; TS018bddb2=01c57796b1ce5e560a3acea5866f130071aba6c94847aef00e2c6a9de2dab8118bfe7121b86cfedb5bc910f183b076dd1bde9c3aa8; CASLLD=2023-10-27T11:35:05; CountryCodeCookie=IT; TS0126ce9e=01c57796b1ce5e560a3acea5866f130071aba6c94847aef00e2c6a9de2dab8118bfe7121b86cfedb5bc910f183b076dd1bde9c3aa8',
        'origin': 'https://sports.williamhill.it',
        'referer': 'https://sports.williamhill.it/betting/it-it',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    params = {
        'service': 'https://sessc-cs.williamhill.it/handle',
    }

    response = requests.get('https://auth.williamhill.it/cas/login', params=params, cookies=cookies, headers=headers)


    ticket = response.json()["serviceTicket"]

    headers = {
        'authority': 'sessc-cs.williamhill.it',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'TS018bddb2=011439b523e7ce1dcaa1d27d1c447d307859ac2a789e28cb18355a5a8287736e03e45a5d2a26abebf7bd8157aa602d9f8cc4231c3b; ddl_landing_document_location=https://sports.williamhill.it/betting/it-it; utag_main=_sn:1$_se:1$_ss:1$_st:1698401197199$ses_id:1698399397199%3Bexp-session$_pn:1%3Bexp-session; GoogleClickId=undefined; CASLLD=2023-10-27T11:35:05; CountryCodeCookie=IT; TS0126ce9e=01c57796b1ce5e560a3acea5866f130071aba6c94847aef00e2c6a9de2dab8118bfe7121b86cfedb5bc910f183b076dd1bde9c3aa8',
        'origin': 'https://sports.williamhill.it',
        'referer': 'https://sports.williamhill.it/betting/it-it',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }



    params = {
        'ticket': ticket
    }

    response = requests.get('https://sessc-cs.williamhill.it/handle', params=params, cookies=cookies, headers=headers)


    cookies = response.cookies.get_dict()

    return cookies


def get_bets(cookies):
    headers = {
        'authority': 'gql-cs.williamhill.it',
        'accept': '*/*',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        # 'cookie': 'ddl_landing_document_location=https://www.williamhill.it/; trk_jsoncookie=%7B%22serveGroup%22%3A32.457872162141555%7D; GoogleClickId=undefined; CountryCodeCookie=IT; cust_lang=it; is_cas=Y; sitePreference=DESKTOP; landingURL=https%3A%2F%2Fsports.williamhill.it%2Fbetting%2Fit-it; trk_uid=05594MN; lastSiteVisited=https://sports.williamhill.it; xsys_balance=; banner_click=NA,NA,NA,NA,admap:d_direct%3Bsource:%3Bzone:%3Bchannel:; banner_domainclick=NA,NA,NA,NA,admap:d_direct%3Bsource:%3Bzone:%3Bchannel:; click_info=pid=0&bid=0; vars_info=; source_NR=NR; CONSENTMGR=consent:true%7Cts:1698305261815%7Cid:018b51f27ec6001fd2cca4c3d4750506f001b06700fb8; _rdt_uuid=1698305261937.5d40495f-53f2-43ae-8fb4-c76c0c60d399; _cs_ex=1658816546; _cs_c=1; _gid=GA1.2.652001140.1698308282; aws_bts=true; hide_header=0; tealium_data=%7B%22effortAttempt%22%3A1%2C%22landingDocumentLocation%22%3A%22https%3A//sports.williamhill.it/bet_ita/it%3Faction%3DDoHistory%26start_day%3D1%26start_month%3D1%26start_year%3D2007%26end_day%3D8%26end_month%3D6%26end_year%3D2018%26txn_type%3DBET_OPEN%26stateTime%3DSELECTION%26_start_day%3D1%26_start_month%3D1%26_start_year%3D2007%26resultsOnly%3D1%26source%3DCP%22%2C%22isExistingPaymentMethodFlag%22%3Anull%2C%22isFirstDeposit%22%3Anull%2C%22isRegistrationDeposit%22%3Afalse%2C%22depStartEventTriggered%22%3Afalse%2C%22loginStatus%22%3A%22Logged%20In%22%7D; wh_device={"is_native":"false","device_os":"desktop","os_version":"0","is_tablet":false}; _cs_mk=0.8385365899027852_1698398160598; _ga=GA1.2.31717655.1698308282; CASLLD=2023-10-27T07:49:37; sc-session=SC-4000557-qqQUSuJ9HAj6Qru4f7q2yjvaAFaH41qus0TcofMvkNU-ip-100-76-146-244.eu-west-1.compute.internal; TS01f9a9d1=01f024109a8db638d543fba8f5010e52ae2365a0de087848d7e05ec24da4db6fccc4757421dae6e0bc2feace6b2b41d5db02e81f98; cas_ssl_login=IwIa45R_hFE815Qsp3AC2Oog8DBps37ZAZwCTJaR9zdZb2sTF0K12_CbSrCrBhpOlPbYUYhrPaScCNvkukzTPblMC3W8xNIY2xla81Oh5OlGVsg9CvqUJc3rSAGL4wZBHkq06rFznzaULhukO~Xh2ktpgU5T~rFWC1UK_CKq5mAcS76mwdHaxmgD7KPQoNNyTaHDRfRL_FTV; cas_login=AVlMmjFixoGcRSdYWiuvAXI+sY0S9g4ugsPShd2ZcOejkgNN8LygRDJgRI7VvkgHn6dx0FTcoZYozmPy6lRH3DFxDX6cP+WMjfM9davN00Cp49MQ06ByEbuxrV3IGLbU7yfrPeg=; cas_ssl_cookie_samesite=AVlMmjFixoGcRSdYWiuvAXI+sY0S9g4ugsPShd2ZcOejkgNN8LygRDJgRI7VvkgHn6dx0FTcoZYozmPy6lRH3DFxDX6cP+WMjfM9davN00Cp49MQ06ByEbuxrV3IGLbU7yfrPeg=; cust_auth=6d5e5b2b7b05a3c662d23794df685dbf2852f88aca10aae09c636e37a91506db1d16130fed00383d4e; cust_login=GRhSrA8vUd5U1bXo/Dk+Xj2He7wbDcC9UqKY+sfTbMdDOWZ4rciLRWksaERHhA725ilxXIdZgnUcwcvRCLhXVQvJdeb2AxEnLZ50urWUyGb3SDtPB0FCfVLdRRf4cnMPlsdpwE44aYUvdH0ovfZaruOwACCip+NKdr11+HMw5HViFiTap0EEBv/SX1JiIirfE8h0pkOSt/hVzkVxkDRJhUAm5JblcQdYHP5xgg==; cust_ssl_login=REklEGgdVR3qa6eQ+ew115PqRN1v6S4x3PuVDLBuEfesaG9fzPiIiPn0j6rx7WRaWDwY1tOHp3/x4Wj40GdBEe26HTQjOW+hBLwa8V2XSv4EvE+HhM5jm5W4; cust_ssl_login_samesite=GRhSrA8vUd5U1bXo/Dk+Xj2He7wbDcC9UqKY+sfTbMdDOWZ4rciLRWksaERHhA725ilxXIdZgnUcwcvRCLhXVQvJdeb2AxEnLZ50urWUyGb3SDtPB0FCfVLdRRf4cnMPlsdpwE44aYUvdH0ovfZaruOwACCip+NKdr11+HMw5HViFiTap0EEBv/SX1JiIirfE8h0pkOSt/hVzkVxkDRJhUAm5JblcQdYHP5xgg==; cust_prefs=it|DECIMAL|form|TYPE|PRICE|||1698352934-0|SB|0|1||0|it|1|TIME|TYPE|0|2|A|0||0|0||TYPE||-|0.00; CSRF_COOKIE=455cf06c0e154e9e1a6a; TS0192828e=0125ced716effbde751cda64d42c523b0de125df4babdc728891060fa7567059d01174a00b2b083b61f0c12e5b2615b2899999ba46; TS014de5c1=0125ced716effbde751cda64d42c523b0de125df4babdc728891060fa7567059d01174a00b2b083b61f0c12e5b2615b2899999ba46; TS0126ce9e=011d058923e2f914cbfa941110774ccfe54b5bd5f450c97cb19519b45643e1b347e4ebde498a512ad52966327f804cb9c174c5b46a; utag_main=v_id:018b51f27ec6001fd2cca4c3d4750506f001b06700fb8$_sn:8$_se:12$_ss:0$_st:1698400462653$dc_visit:8$ses_id:1698398159656%3Bexp-session$_pn:1%3Bexp-session$dc_event:2%3Bexp-session; _gat_gtag_UA_136626402_3=1; _ga_Q5E35JEC8M=GS1.1.1698398161.6.1.1698398662.0.0.0',
        'origin': 'https://sports.williamhill.it',
        'referer': 'https://sports.williamhill.it/betting/it-it',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'vertical': 'sportsbook',
    }

    json_data = {
        'operationName': 'TransactionsQuery',
        'variables': {
            'pagingToken': {
                'pageSize': 20,
            },
            'filters': {
                'datePredefined': 'DAYS_30',
                'filterType': [
                    'ALL',
                ],
                'filterGroup': 'ALL',
            },
        },
        'query': 'query TransactionsQuery($pagingToken: MyAccountTransactionsPagingFilter, $filters: MyAccountTransactionFilters) {\n  transactions(pagingToken: $pagingToken, filters: $filters) {\n    pagingToken {\n      pageSize\n      paginationToken\n      lastItemId\n      __typename\n    }\n    transactions {\n      __typename\n      id\n      transactionType\n      date\n      reference\n      ... on MyAccountTransactionSport {\n        aamsId\n        sort\n        type\n        stake\n        stakePerLine\n        returns\n        flags\n        result\n        boostedBetDetails {\n          originalPrice\n          enhancedPrice\n          __typename\n        }\n        eachWay\n        freeStake\n        numberOfLines\n        legs {\n          parts {\n            event\n            market\n            selection\n            price\n            result\n            eachWayConditions {\n              places\n              price\n              __typename\n            }\n            handicap\n            __typename\n          }\n          __typename\n        }\n        showToteIcon\n        shopDetails {\n          shopNumber\n          __typename\n        }\n        __typename\n      }\n      ... on MyAccountTransactionPayment {\n        description\n        amount\n        paymentMethod {\n          type\n          __typename\n        }\n        __typename\n      }\n      ... on MyAccountTransactionManualAdjustment {\n        description\n        amount\n        label\n        __typename\n      }\n      ... on MyAccountTransactionCasino {\n        type\n        description\n        amount\n        freeAmount\n        __typename\n      }\n      ... on MyAccountTransactionSlots {\n        type\n        description\n        amount\n        freeAmount\n        __typename\n      }\n      ... on MyAccountTransactionVegas {\n        type\n        description\n        amount\n        freeAmount\n        __typename\n      }\n      ... on MyAccountTransactionPoker {\n        type\n        description\n        amount\n        freeAmount\n        __typename\n      }\n      ... on MyAccountTransactionBingo {\n        type\n        description\n        amount\n        freeAmount\n        __typename\n      }\n      ... on MyAccountTransactionLiveCasino {\n        type\n        description\n        amount\n        freeAmount\n        __typename\n      }\n      ... on MyAccountTransactionGames {\n        type\n        description\n        amount\n        freeAmount\n        __typename\n      }\n      ... on MyAccountTransactionGaming {\n        type\n        description\n        amount\n        __typename\n      }\n      ... on MyAccountTransactionSpanishFunds {\n        description\n        amount\n        __typename\n      }\n      ... on MyAccountTransactionLotteryBet {\n        amount\n        lotteryName\n        stake\n        returns\n        subscription {\n          drawName\n          selectedPicks\n          draw {\n            drawDate\n            resultPicks\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n    }\n    __typename\n  }\n}\n',
    }

    import requests

    response = requests.post('https://gql-cs.williamhill.it/graphql', cookies=cookies, headers=headers, json=json_data)

    transactions = []

    import util

    for transaction in response.json()["data"]["transactions"]["transactions"]:

        if transaction["__typename"] == "MyAccountTransactionPayment":
            continue

        simplified_transaction = util.sheet_bet('planetwin365', transaction["transactionType"], transaction["stake"], transaction["returns"], transaction["result"], transaction["date"], transaction["date"])

        # simplified_transaction = {
        #     "id": transaction["id"],
        #     "transactionType": transaction["transactionType"],
        #     "date": transaction["date"],
        #     "stake": transaction["stake"],
        #     "returns": transaction["returns"],
        #     "result": transaction["result"],
        # }
        transactions.append(simplified_transaction)

    return transactions

    import requests

    headers = {
        'authority': 'transact.williamhill.it',
        'accept': 'text/event-stream',
        'accept-language': 'it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        # 'cookie': 'ddl_landing_document_location=https://sports.williamhill.it/betting/it-it; GoogleClickId=undefined; CountryCodeCookie=IT; cust_lang=it; is_cas=Y; sitePreference=DESKTOP; cust_auth=6d5e5b2b7b05a2cb158c5eb07b8f8dffe49b7123e16d443ccdeeec0f98e1f31f657b61130ae2d123c5; trk_uid=05594MN; landingURL=https%3A%2F%2Fsports.williamhill.it%2Fbetting%2Fit-it; tealium_data=%7B%22effortAttempt%22%3A1%2C%22landingDocumentLocation%22%3A%22https%3A//sports.williamhill.it/bet_ita/it%3Faction%3DGoHistory%22%2C%22isExistingPaymentMethodFlag%22%3Anull%2C%22isFirstDeposit%22%3Anull%2C%22isRegistrationDeposit%22%3Afalse%2C%22depStartEventTriggered%22%3Afalse%2C%22loginStatus%22%3A%22Logged%20In%22%7D; trk_jsoncookie=%7B%22serveGroup%22%3A75.52131307437773%7D; TS01f9a9d1=01975f9014955984c7904cc9287547f2fac9e4ae2b8bc7be37604386e159f3201397472d4cd3611e6112119d51994e512cb4384e21; xsys_balance=; SKIP_CAS_GUEST_SESSION_CHECK=Y; CASLLD=2023-10-27T11:50:38; sc-session=SC-4002199---ncmjWPdaRAY8CD9P6zjp-P5A--Fmwt9da2IeLgYpw-ip-100-76-146-244.eu-west-1.compute.internal; cas_ssl_login=mWRR13A_Ib~mFmSKIhHMrU~7MdGnBuhIKaHkvyxz~0tnksR3ty_I_gUdFYsoRb~4xep0gDUvOlatVLUF4~vBonZks84fAEF8yTcYY2vfwBAnori83qpoREjJFrk1JFCXIGPLiZkL2oGLbr3jQJnGNzjFxiy5zc4fOvaBLaRdA9TpijeLQnxUsL6JplWOqw5tdDIdF3MKWpVt; cas_login=AVk6QWLIIKWtZmmwUNa2h0TprDbjqP3Z+XOlIdXXjQTp3iAy9bL5outNBi/n57OyHt3w5tjfRWuuAeSEuVx053O9jDJl0pNoKYL5wIy/SOeTyn7YEEaScFsujaJ0TR/MG+Vn24s=; cas_ssl_cookie_samesite=AVk6QWLIIKWtZmmwUNa2h0TprDbjqP3Z+XOlIdXXjQTp3iAy9bL5outNBi/n57OyHt3w5tjfRWuuAeSEuVx053O9jDJl0pNoKYL5wIy/SOeTyn7YEEaScFsujaJ0TR/MG+Vn24s=; cust_login=AQJe0hQ3L7BcW1/A8/nAlxcTr9ztRH3t1u3O6C+AUSrDALtgjjUTiVVkgybE1Emxj0+phbIyWIn8jZUO2z0o1Q+YDvnCYQibFrTWcDsqAjpJnlj6GZ/DTxm5a/pGFTU45Ci9R8jA8vIC40x/93UJCccXpunSpwd8oJmX5Nmyud1KnnzsE4CnGaeGIPJyh3TdiYsXyrDv8UUVVzyt6mJxgLXJW8RVjUxu0AZTFg==; cust_ssl_login=e243aAYzWX7Cuwdl0lbsramY64O/1DH2REzqkdIwacVHVbs4lfE14Ju2IFCcuqlr2IL+f70fMOSyFUgR228lnqVtKC1ej8wUEEaroZmftmC8VHHFPo07cYlf; cust_ssl_login_samesite=AQJe0hQ3L7BcW1/A8/nAlxcTr9ztRH3t1u3O6C+AUSrDALtgjjUTiVVkgybE1Emxj0+phbIyWIn8jZUO2z0o1Q+YDvnCYQibFrTWcDsqAjpJnlj6GZ/DTxm5a/pGFTU45Ci9R8jA8vIC40x/93UJCccXpunSpwd8oJmX5Nmyud1KnnzsE4CnGaeGIPJyh3TdiYsXyrDv8UUVVzyt6mJxgLXJW8RVjUxu0AZTFg==; cust_prefs=it|DECIMAL|form|TYPE|PRICE|||1698401417-0|SB|0|1||0|it|1|TIME|TYPE|0|2|A|0||0|0||TYPE||-|0.00; CSRF_COOKIE=1abdb24306676137d8d7; TS0192828e=01bfe923808a394006e577ba2e8779580553d7d7799d34f701f8ec7046a8c7ce1bd6ecd29c2c846a133b37d3bfd2e8912a8a83371e; TS014de5c1=01bfe923808a394006e577ba2e8779580553d7d7799d34f701f8ec7046a8c7ce1bd6ecd29c2c846a133b37d3bfd2e8912a8a83371e; TS0126ce9e=01e1055e9c307b4872334725b698cc5f3da7c4c3f1357fc8a65861d66dd30c77f78d22a0759ddeafe38fca5c2b225d559c9456ad83; utag_main=_sn:1$_se:22$_ss:0$_st:1698402380193$ses_id:1698399397199%3Bexp-session$_pn:3%3Bexp-session$dc_visit:1$dc_event:2%3Bexp-session$v_id:018b708f380a0010fcf3f76b5f100506f003906700fb8; SESSION=OTQ1OWI2NDEtM2Y1My00YzQzLWIwZGQtYjQ1OTc3YTE2NWJk; TS018bddb2=01c240e3b3e0f2d75d2c1c5909c777e075dbebf99f3761b73138aa5d4cb33cf96f6d075a3818dd7549b8662c0c166f76953f2419bc',
        'origin': 'null',
        'referer': 'https://sports.williamhill.it/betting/it-it',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    }

    params = {
        'lang': 'it',
        'settled': 'false',
        'cashout': 'false',
    }

    import sseclient

    response = requests.get('https://transact.williamhill.it/betslip/sse/bets', params=params, cookies=cookies,
                            stream=True,headers=headers)

    print(response.status_code)
    print(response.text)

    client = sseclient.SSEClient(response)

    bets = []

    for event in client.events():
        if "{" in event.data:
            bet = json.loads(event.data)
            client.close()
    # update cookies file
    with open("cookies_WH.JSON", "w") as f:
        json.dump(cookies, f)

    return bets



def main():
    # get cookies from William Hill Cookies file
    with open("cookies_WH.JSON", "r") as f:
        cookies = json.load(f)

    try:
        return get_bets(cookies)
    except Exception as e:
        print("Error WilliamHill: ", e)
        cookies = get_sc_session()
        print("New WH cookies: ", cookies)
        return get_bets(cookies)




