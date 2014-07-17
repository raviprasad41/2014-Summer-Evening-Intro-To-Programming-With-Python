class Stock():
    def __init__(self, ticker_symbol):
        self.ticker_symbol = ticker_symbol
        self.historical_quotes = []
    def moving_average(self):
        pass
class Quote():
    def __init__(self, closing_price, quote_date):
        self.closing_price = closing_price
        self.quote_date = quote_date
class StocksModel():
    stocks = {}
    def load(self, data):
        for record in data:
            date = record[0]
            symbol = record[1]
            price = record[2]
            if not self.stocks.has_key(symbol):
                self.stocks[symbol] = Stock(symbol)
            stock = self.stocks[symbol]
            stock.historical_quotes.append( Quote(price, date) )
class StocksView():
    def render(self,stocks):
        for k,v in stocks:
            print k
            for q in s.historical_quotes:
                print q.quote_date + "-" + q.closing_price
test_data = [
    ["2014-06-01", "APPL",100.10],
    ["2014-06-02", "APPL",110.60],
    ["2014-06-03", "APPL",120.20],
    ["2014-06-04", "APPL",100.50],
]
model = StocksModel()
model.load(test_data)
view = StocksView()
view.render(model.stocks)