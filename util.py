class sheet_bet:
    def __init__(self, bookmaker, bet_type, bet, odds, result, place_date, event_date):
        self.bookmaker = bookmaker
        self.bet_type = bet_type
        self.bet = bet
        self.odds = odds
        self.result = result
        self.place_date = place_date
        self.event_date = event_date

    def __str__(self):
        return f'{self.bookmaker} {self.bet_type} {self.bet} {self.odds} {self.result} {self.place_date} {self.event_date}'


