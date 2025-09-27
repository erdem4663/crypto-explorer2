import requests

def get_price(symbol="bitcoin"):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": symbol, "vs_currencies": "usd"}
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    return data.get(symbol, {}).get("usd")

if __name__ == "__main__":
    print("BTC price (USD):", get_price("bitcoin"))
