from polygon import RESTClient

client = RESTClient("y0pnIt8YeMJpLoSTQyFzTjU1vXPpsXlM")

aggs = []
for a in client.list_aggs(
    "AAPL",
    1,
    "minute",
    "2022-01-01",
    "2023-02-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)

#use X and polygon API to give information on inputed stock and use X sentiment analysis to make predictions