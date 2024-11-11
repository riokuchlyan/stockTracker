from polygon import RESTClient

client = RESTClient("y0pnIt8YeMJpLoSTQyFzTjU1vXPpsXlM")

def getStockData(stocksTicker, date):
    information = client.get_daily_open_close_agg(stocksTicker.upper(), date)
    return str(information).split(", ")[3:7]


print(getStockData("aapl", "2024-11-08"))
#use X and polygon API to give information on inputed stock and use X sentiment analysis to make predictions