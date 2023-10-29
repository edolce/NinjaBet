from googleapiclient.discovery import build
from google.oauth2 import service_account
import requests
import datetime
from time import sleep
import json


def strike(value):
    str_value = str(int(float(value) * 1000))

    while len(str_value) <= 7:
        str_value = '0' + str_value

    return str_value


class SpreadSheets:
    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'keys.json'
        creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        # The ID and range of a sample spreadsheet.
        self.SAMPLE_SPREADSHEET_ID = '1LxYQ2QIrAxbYXMeVYnt__aoyXiqx45wcczRWKZKP604'
        service = build('sheets', 'v4', credentials=creds)
        # Call the Sheets API
        self.sheet = service.spreadsheets()
        result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range="A1:AC1000").execute()
        values = result.get('values', [])
        print(values)

        # Data da aggiungere
        data = {'historyCoupons': [{'couponRef': 6339829178, 'couponExternalRef': 'cc1b2858-f4d6-4717-ab64-5a67ede169e2', 'placedDate': '2023-10-24T10:11:09.781Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': [], 'bets': [{'betRef': 9427795530, 'couponRowIndexes': [0], 'betOdds': 5750, 'betOddsBoosted': 6700, 'playedOdds': 5750, 'betStatus': 'WON', 'stake': 20000, 'payout': 134000, 'potentialPayout': 115000, 'potentialPayoutBoosted': 134000, 'bonusPayout': 19000, 'tags': [], 'localLicenseReference': 'df07e70a191fb049150c'}], 'outcomes': [{'outcomeId': 3324648502, 'eventId': 1020070835, 'betOfferId': 2400408713, 'label': 'Borussia Dortmund', 'settledInfo': {'result': {'score': '0-1', 'correct': ['2'], 'scratched': []}}, 'status': 'WON', 'participantId': 1000000110, 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3324648502, 'status': 'WON', 'playedOdds': 5750, 'payoutOdds': 5750, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1020070835, 'sport': 'FOOTBALL', 'homeName': 'Newcastle United', 'awayName': 'Borussia Dortmund', 'eventName': 'Newcastle United - Borussia Dortmund', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000093381, 'name': 'Champions League'}], 'eventStartDate': '2023-10-25T19:00:00Z'}], 'betOffers': [{'betOfferId': 2400408713, 'boType': 'Match', 'boTypeId': 2, 'criterion': 'Esito Finale 1X2', 'tags': []}], 'bonusPayout': 19000, 'rewardType': 'PROFIT_BOOST', 'boostPercentage': 20}, {'couponRef': 6334418335, 'couponExternalRef': 'f808b4b6-3e81-497e-a896-3ce351809c56', 'placedDate': '2023-10-22T19:25:13.684Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': [], 'bets': [{'betRef': 9421936652, 'couponRowIndexes': [0], 'betOdds': 0, 'playedOdds': 1880, 'betStatus': 'LOST', 'stake': 100000, 'payout': 0, 'potentialPayout': 0, 'tags': [], 'localLicenseReference': 'df07e70a16200b372504'}], 'outcomes': [{'outcomeId': 3329298798, 'eventId': 1019426535, 'betOfferId': 2401953249, 'label': 'Over 2.5', 'settledInfo': {'result': {'score': '', 'correct': ['Under'], 'scratched': []}}, 'status': 'LOST', 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3329298798, 'status': 'LOST', 'playedOdds': 1880, 'payoutOdds': 0, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1019426535, 'sport': 'FOOTBALL', 'homeName': 'Bragantino-SP', 'awayName': 'Fluminense-RJ', 'eventName': 'Bragantino-SP - Fluminense-RJ', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461741, 'name': 'Brasile'}, {'id': 1000094569, 'name': 'Brasileirao Serie A'}], 'eventStartDate': '2023-10-22T21:30:00Z'}], 'betOffers': [{'betOfferId': 2401953249, 'boType': 'Over/Under', 'boTypeId': 6, 'criterion': 'Totale gol', 'line': 2500, 'tags': []}]}, {'couponRef': 6331873896, 'couponExternalRef': 'f5539446-49e5-45ca-90cf-e2c725e25b96', 'placedDate': '2023-10-22T12:46:11.178Z', 'currency': 'EUR', 'channel': 'MOBILE', 'tags': [], 'bets': [{'betRef': 9419164386, 'couponRowIndexes': [0], 'betOdds': 2170, 'playedOdds': 2170, 'betStatus': 'WON', 'stake': 130000, 'payout': 282100, 'potentialPayout': 282100, 'tags': [], 'localLicenseReference': 'df07e70a161fa7e8c30a'}], 'outcomes': [{'outcomeId': 3326457202, 'eventId': 1019901677, 'betOfferId': 2401000097, 'label': 'Over 2.5', 'settledInfo': {'result': {'score': '', 'correct': ['Over'], 'scratched': []}}, 'status': 'WON', 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3326457202, 'status': 'WON', 'playedOdds': 2170, 'payoutOdds': 2170, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1019901677, 'sport': 'FOOTBALL', 'homeName': 'Salernitana', 'awayName': 'Cagliari', 'eventName': 'Salernitana - Cagliari', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461745, 'name': 'Italia'}, {'id': 1000095001, 'name': 'Serie A'}], 'eventStartDate': '2023-10-22T13:00:00Z'}], 'betOffers': [{'betOfferId': 2401000097, 'boType': 'Over/Under', 'boTypeId': 6, 'criterion': 'Totale gol', 'line': 2500, 'tags': []}]}, {'couponRef': 6330750377, 'couponExternalRef': '1aa2f01d-b5f2-43ed-b2f2-5d580193f755-pba', 'placedDate': '2023-10-22T06:05:50.04Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': ['PBA_BETS'], 'bets': [{'betRef': 9417849830, 'couponRowIndexes': [0], 'betOdds': 0, 'playedOdds': 2500, 'betStatus': 'LOST', 'stake': 150000, 'requestedStake': 150000, 'payout': 0, 'potentialPayout': 0, 'tags': [], 'localLicenseReference': 'df07e70a162003f8d805'}], 'outcomes': [{'outcomeId': 3330267617, 'eventId': 1020184593, 'betOfferId': 2402252819, 'label': 'Si', 'settledInfo': {'result': {'score': '', 'correct': ['No'], 'scratched': []}}, 'status': 'LOST', 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3330267617, 'status': 'LOST', 'playedOdds': 2500, 'payoutOdds': 0, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1020184593, 'sport': 'FOOTBALL', 'homeName': 'Asteras Tripolis', 'awayName': 'AEK Atene', 'eventName': 'Asteras Tripolis - AEK Atene', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461752, 'name': 'Grecia'}, {'id': 1000094996, 'name': 'Super League'}], 'eventStartDate': '2023-10-22T13:00:00Z'}], 'betOffers': [{'betOfferId': 2402252819, 'boType': 'Yes/No', 'boTypeId': 18, 'criterion': 'Entrambe le squadre a segno (Gol/No Gol)', 'tags': []}]}, {'couponRef': 6330749171, 'couponExternalRef': '696743ef-32a0-453c-a31a-96f5b78c5ac1', 'placedDate': '2023-10-22T06:00:47.145Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': [], 'bets': [{'betRef': 9417796361, 'couponRowIndexes': [0], 'betOdds': 2060, 'playedOdds': 2060, 'betStatus': 'WON', 'stake': 150000, 'payout': 309000, 'potentialPayout': 309000, 'tags': [], 'localLicenseReference': 'df07e70a161fa3bf2709'}], 'outcomes': [{'outcomeId': 3331712161, 'eventId': 1020197880, 'betOfferId': 2402743475, 'label': 'Under 2.5', 'settledInfo': {'result': {'score': '', 'correct': ['Under'], 'scratched': []}}, 'status': 'WON', 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3331712161, 'status': 'WON', 'playedOdds': 2060, 'payoutOdds': 2060, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1020197880, 'sport': 'FOOTBALL', 'homeName': 'UC Dublin', 'awayName': 'Cork City', 'eventName': 'UC Dublin - Cork City', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461750, 'name': 'Irlanda'}, {'id': 1000095601, 'name': 'Premier Division'}], 'eventStartDate': '2023-10-22T14:00:00Z'}], 'betOffers': [{'betOfferId': 2402743475, 'boType': 'Over/Under', 'boTypeId': 6, 'criterion': 'Totale gol', 'line': 2500, 'tags': []}]}, {'couponRef': 6330691139, 'couponExternalRef': '21622901-f325-4563-85d6-b21a86c6e44e', 'placedDate': '2023-10-22T05:28:13.352Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': [], 'bets': [{'betRef': 9417737566, 'couponRowIndexes': [0], 'betOdds': 0, 'playedOdds': 4300, 'betStatus': 'LOST', 'stake': 150000, 'payout': 0, 'potentialPayout': 0, 'tags': [], 'localLicenseReference': 'df07e70a162003e7b004'}], 'outcomes': [{'outcomeId': 3326456278, 'eventId': 1019901673, 'betOfferId': 2400999699, 'label': 'X', 'settledInfo': {'result': {'score': '1-0', 'correct': ['1'], 'scratched': []}}, 'status': 'LOST', 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3326456278, 'status': 'LOST', 'playedOdds': 4300, 'payoutOdds': 0, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1019901673, 'sport': 'FOOTBALL', 'homeName': 'Roma', 'awayName': 'Monza', 'eventName': 'Roma - Monza', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461745, 'name': 'Italia'}, {'id': 1000095001, 'name': 'Serie A'}], 'eventStartDate': '2023-10-22T10:30:00Z'}], 'betOffers': [{'betOfferId': 2400999699, 'boType': 'Match', 'boTypeId': 2, 'criterion': 'Esito Finale 1X2', 'tags': []}]}, {'couponRef': 6328970109, 'couponExternalRef': 'fad4157e-e89e-4ae9-95b0-d8f2341eef09-pba', 'placedDate': '2023-10-21T21:02:50.6Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': ['PBA_BETS'], 'bets': [{'betRef': 9415865354, 'couponRowIndexes': [0], 'betOdds': 3300, 'playedOdds': 3300, 'betStatus': 'WON', 'stake': 150000, 'requestedStake': 150000, 'payout': 495000, 'potentialPayout': 495000, 'tags': [], 'localLicenseReference': 'df07e70a152003638705'}], 'outcomes': [{'outcomeId': 3329280486, 'eventId': 1019426557, 'betOfferId': 2401918590, 'label': 'X', 'settledInfo': {'result': {'score': '1-1', 'correct': ['X'], 'scratched': []}}, 'status': 'WON', 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3329280486, 'status': 'WON', 'playedOdds': 3300, 'payoutOdds': 3300, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1019426557, 'sport': 'FOOTBALL', 'homeName': 'Cuiabá-MT', 'awayName': 'Goiás-GO', 'eventName': 'Cuiabá-MT - Goiás-GO', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461741, 'name': 'Brasile'}, {'id': 1000094569, 'name': 'Brasileirao Serie A'}], 'eventStartDate': '2023-10-21T21:30:00Z'}], 'betOffers': [{'betOfferId': 2401918590, 'boType': 'Match', 'boTypeId': 2, 'criterion': 'Esito Finale 1X2', 'tags': []}]}, {'couponRef': 6328338881, 'couponExternalRef': 'eeffacb8-342c-448e-80d5-be3ccd6dfc87-pba', 'placedDate': '2023-10-21T19:10:40.196Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': ['PBA_BETS'], 'bets': [{'betRef': 9415210970, 'couponRowIndexes': [0], 'betOdds': 0, 'playedOdds': 3100, 'betStatus': 'LOST', 'stake': 150000, 'requestedStake': 150000, 'payout': 0, 'potentialPayout': 0, 'tags': [], 'localLicenseReference': 'df07e70a162002f28004'}], 'outcomes': [{'outcomeId': 3329379375, 'eventId': 1019281328, 'betOfferId': 2401952817, 'label': 'Toronto FC', 'settledInfo': {'result': {'score': '0-2', 'correct': ['2'], 'scratched': []}}, 'status': 'LOST', 'participantId': 1000129223, 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3329379375, 'status': 'LOST', 'playedOdds': 3100, 'payoutOdds': 0, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1019281328, 'sport': 'FOOTBALL', 'homeName': 'Toronto FC', 'awayName': 'Orlando City', 'eventName': 'Toronto FC - Orlando City', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461816, 'name': 'USA'}, {'id': 1000095063, 'name': 'MLS'}], 'eventStartDate': '2023-10-21T22:00:00Z'}], 'betOffers': [{'betOfferId': 2401952817, 'boType': 'Match', 'boTypeId': 2, 'criterion': 'Esito Finale 1X2', 'tags': []}]}, {'couponRef': 6328217882, 'couponExternalRef': '17d714f9-face-40a6-90e1-3c31bba3e735', 'placedDate': '2023-10-21T18:53:55.537Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': [], 'bets': [{'betRef': 9415045637, 'couponRowIndexes': [0], 'betOdds': 0, 'playedOdds': 2230, 'betStatus': 'LOST', 'stake': 150000, 'payout': 0, 'potentialPayout': 0, 'tags': [], 'localLicenseReference': 'df07e70a161fa2b4bf0b'}], 'outcomes': [{'outcomeId': 3326364206, 'eventId': 1019732460, 'betOfferId': 2400976954, 'label': 'No', 'settledInfo': {'result': {'score': '', 'correct': ['Si'], 'scratched': []}}, 'status': 'LOST', 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3326364206, 'status': 'LOST', 'playedOdds': 2230, 'payoutOdds': 0, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1019732460, 'sport': 'FOOTBALL', 'homeName': 'Randers FC', 'awayName': 'Brøndby IF', 'eventName': 'Randers FC - Brøndby IF', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461736, 'name': 'Danimarca'}, {'id': 1000094978, 'name': 'Superligaen'}], 'eventStartDate': '2023-10-22T16:00:00Z'}], 'betOffers': [{'betOfferId': 2400976954, 'boType': 'Yes/No', 'boTypeId': 18, 'criterion': 'Entrambe le squadre a segno (Gol/No Gol)', 'tags': []}]}, {'couponRef': 6327451032, 'couponExternalRef': '08637942-6642-4da7-961b-49c69cb12ab3', 'placedDate': '2023-10-21T17:07:11.543Z', 'currency': 'EUR', 'channel': 'WEB', 'tags': [], 'bets': [{'betRef': 9414204677, 'couponRowIndexes': [0], 'betOdds': 0, 'playedOdds': 2950, 'betStatus': 'LOST', 'stake': 300000, 'payout': 0, 'potentialPayout': 0, 'tags': [], 'localLicenseReference': 'df07e70a152002125804'}], 'outcomes': [{'outcomeId': 3326424672, 'eventId': 1019901701, 'betOfferId': 2400978606, 'label': 'Sassuolo', 'settledInfo': {'result': {'score': '0-2', 'correct': ['2'], 'scratched': []}}, 'status': 'LOST', 'participantId': 1000063908, 'outcomeTags': []}], 'couponRows': [{'index': 0, 'outcomeId': 3326424672, 'status': 'LOST', 'playedOdds': 2950, 'payoutOdds': 0, 'bestOddsGuaranteed': False, 'tags': [], 'selectionType': 'SIMPLE'}], 'events': [{'eventId': 1019901701, 'sport': 'FOOTBALL', 'homeName': 'Sassuolo', 'awayName': 'Lazio', 'eventName': 'Sassuolo - Lazio', 'eventGroups': [{'id': 1000093190, 'name': 'Calcio'}, {'id': 1000461745, 'name': 'Italia'}, {'id': 1000095001, 'name': 'Serie A'}], 'eventStartDate': '2023-10-21T18:45:00Z'}], 'betOffers': [{'betOfferId': 2400978606, 'boType': 'Match', 'boTypeId': 2, 'criterion': 'Esito Finale 1X2', 'tags': []}]}], 'range': {'start': 0, 'size': 10, 'more': False}}

    def save(self, simplified_data):



        # Prepare the request to update values in the spreadsheet
        request_body = {
            "values": simplified_data
        }

        #check first empty row
        result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range="A1:AC1000").execute()
        values = result.get('values', [])

        row_number = 0
        try:
            while not values[row_number][0] is None:
                row_number += 1
        except Exception as e:
            pass

        # Execute the request to update the spreadsheet
        self.sheet.values().update(
            spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
            range="A"+str(row_number+1),
            valueInputOption="USER_ENTERED",
            body=request_body
        ).execute()

        #self.sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,range="A1",valueInputOption="USER_ENTERED", body={"values": [[2,3]]}).execute()

        print("I dati sono stati aggiunti al foglio Google.")


    #
    # def get_rows(self):
    #     result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID, range="A1:AC1000").execute()
    #     values = result.get('values', [])
    #     row_number = 0
    #     try:
    #         while not values[row_number][0] is None:
    #             row_number += 1
    #     except Exception as e:
    #         pass
    #
    #     rows = []
    #     for row_n in range(1, row_number):
    #         rows.append(values[row_n])
    #
    #     return rows
    #
    # def control_live(self, rows):
    #     for row in rows:
    #         try:
    #             date = datetime.datetime.strptime(row[5], "%Y-%m-%d")
    #             date = date.strftime("%y%m%d")
    #
    #             full_symbol = str(row[2]) + str(date) + str(row[4]).lower()[0] + strike(str(row[6]))
    #
    #             response = requests.get('https://sandbox.tradier.com/v1/markets/quotes',
    #                                     params={'symbols': str(row[2]) + ',' + full_symbol, 'greeks': 'false'},
    #                                     headers={'Authorization': 'Bearer %s' % token, 'Accept': 'application/json'}
    #                                     )
    #             json_response = response.json()
    #
    #             if len(row) <= 16:
    #                 row.append(json_response['quotes']['quote'][1]['last'])
    #             else:
    #                 row[16] = json_response['quotes']['quote'][1]['last']
    #
    #             if len(row) <= 17:
    #                 row.append(json_response['quotes']['quote'][0]['last'])
    #             else:
    #                 row[17] = json_response['quotes']['quote'][0]['last']
    #
    #             # Get raw number
    #             result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
    #                                              range="A1:AC1000").execute()
    #             values = result.get('values', [])
    #
    #             row_number = 999
    #
    #             for index in range(len(values)):
    #                 if values[index][0] == row[0]:
    #                     row_number = index
    #                     break
    #
    #             self.sheet.values().update(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
    #                                        range="A" + str(row_number + 1),
    #                                        valueInputOption="USER_ENTERED", body={"values": [list(row)]}).execute()
    #         except Exception:
    #             # Get raw number
    #             result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
    #                                              range="A1:AC1000").execute()
    #             values = result.get('values', [])
    #
    #             row_number = 999
    #
    #             for index in range(len(values)):
    #                 if values[index][0] == row[0]:
    #                     row_number = index
    #                     break
    #             # print("A row maybe is expired or another problem occurred [Row:%s]" % str(row_number + 1))
    #             # traceback.print_exc()


if __name__ == '__main__':
    SpreadSheets()