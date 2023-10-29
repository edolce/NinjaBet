import WilliamHill
import betfair
import leovegas
import planetwin365


bookmakers = {
    'WilliamHill': WilliamHill.main,
    'leovegas': leovegas.main,
    'planetwin365': planetwin365.main,
    'betfair': betfair.main
}

import sheets

if __name__ == '__main__':
    bets = {}
    for bookmaker in bookmakers.keys():
        bets[bookmaker] = bookmakers[bookmaker]()

    sheet0 = sheets.SpreadSheets()

    array_bet = []
    for bookmaker in bets.keys():

        for bet in bets[bookmaker]:
            if isinstance(bet,str):
                continue
            if bet is None:
                continue
            print(bet)
            array_bet.append(
                [
                    bookmaker,
                    bet.bet_type,
                    bet.bet,
                    bet.odds,
                    bet.result,
                    bet.place_date,
                    bet.event_date
                ]
            )
    print(array_bet)
    sheet0.save(array_bet)
