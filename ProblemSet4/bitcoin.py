import requests
import sys

try:
    quantity = float(sys.argv[1])
except TypeError:
    sys.exit("Comand-line arguemnt is not a float")
else:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    rate = response["bpi"]["USD"]["rate_float"]
    amount = rate * quantity
    print(f"${amount:,.4f}")
