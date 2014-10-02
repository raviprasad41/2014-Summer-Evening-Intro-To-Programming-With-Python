import json

f = open("example.json")

data = json.load(f)

for candle in data["candles"]:
    print candle["openBid"]

