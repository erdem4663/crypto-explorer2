import argparse
from fetcher import get_price

def main():
    parser = argparse.ArgumentParser(description="Crypto Explorer CLI")
    parser.add_argument("--symbol", default="bitcoin", help="coin id e.g. bitcoin, ethereum")
    args = parser.parse_args()
    price = get_price(args.symbol)
    if price is None:
        print(f"No price found for {args.symbol}")
    else:
        print(f"{args.symbol} price (USD): {price}")

if __name__ == "__main__":
    main()
