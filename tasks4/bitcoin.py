import requests
import sys

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Can't get response")

response_json = response.json()
rate = response_json["bpi"]["USD"]["rate_float"]
print(f"${rate*n:,.4f}")
