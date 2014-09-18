__author__ = 'kevin'

class CandleType():
    name = "type name"

class Candle(models.Model):
    type = "generic"
    open = 4
    close = 5
    high = 6
    low = 3
    def __init__(self, type="generic", open=0, close=0, high=0, low=0):
        self.type = type
        ...

class MidCandle(Candle):
    type = "mid"

class AskCandle(Candle):
    type = "ask"

class BidCandle(Candle):
    type = "bid"


candles = []

candles.append( Candle("bid",111) )

c = Candle()
c.type = "bid"
c.open = 555
candles.append( c )
