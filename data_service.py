import cryptowatch as cw
#TODO Access API to get data
#TODO Create database tables to store data
#TODO Store Data In tables
#TODO run the service every minute



def get_price(code: str):
    response = cw.markets.get(code)
    return response.market.price.last

print(get_price("KRAKEN:BTCUSD"))