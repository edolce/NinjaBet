import WilliamHill
import betfair
import leovegas
import planetwin365


bookmakers = {
    'WilliamHill': WilliamHill.main,
    'betfair': betfair.main,
    'leovegas': leovegas.main,
    'planetwin365': planetwin365.main
}


if __name__ == '__main__':
    bets = {}
    for bookmaker in bookmakers.keys():
        bets[bookmaker] = bookmakers[bookmaker]()
    print(bets)
