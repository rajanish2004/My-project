import sys
import requests

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data['bpi']['USD']['rate_float']
    except requests.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        sys.exit(1)
    except KeyError:
        print("Error: Unexpected response format from API")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python bitcoin.py <btc_amount>")
        sys.exit(1)

    btc_amount_str = sys.argv[1]

    try:
        btc_amount = float(btc_amount_str)
    except ValueError:
        print("Error: Bitcoin amount must be a valid number")
        sys.exit(1)

    if btc_amount <= 0:
        print("Error: Bitcoin amount must be greater than zero")
        sys.exit(1)

    bitcoin_price = get_bitcoin_price()
    total_cost = btc_amount * bitcoin_price

    # Format total cost to 4 decimal places with commas as thousands separators
    formatted_cost = f"{total_cost:,.4f}"

    print(f"The cost of {btc_amount} Bitcoins is ${formatted_cost} USD")

if __name__ == "__main__":
    main()
