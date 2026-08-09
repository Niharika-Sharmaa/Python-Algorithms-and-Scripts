import requests

print("=" * 40)
print("       CURRENCY CONVERTER")
print("=" * 40)

print("\nAvailable currencies:")
print("USD - US Dollar")
print("INR - Indian Rupee")
print("EUR - Euro")
print("GBP - British Pound")
print("JPY - Japanese Yen")
print("AUD - Australian Dollar")
print("CAD - Canadian Dollar")

while True:
    try:
        amount = float(input("\nEnter amount: "))

        if amount <= 0:
            print("Please enter an amount greater than 0.")
            continue

        from_currency = input("From currency: ").upper()
        to_currency = input("To currency: ").upper()

        print("\nFetching latest exchange rate...")

        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("Invalid currency or unable to get exchange rate.")
            continue

        data = response.json()

        if to_currency not in data["rates"]:
            print("Currency conversion not available.")
            continue

        converted_amount = data["rates"][to_currency]
        exchange_rate = converted_amount / amount

        print("\n" + "-" * 40)
        print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
        print(f"Exchange Rate: 1 {from_currency} = {exchange_rate:.4f} {to_currency}")
        print("-" * 40)

    except ValueError:
        print("Invalid amount. Please enter a number.")

    except requests.exceptions.RequestException:
        print("Unable to connect to the currency API.")
        print("Please check your internet connection.")

    choice = input("\nDo you want to convert another amount? (y/n): ").lower()

    if choice != "y":
        print("\nThank you for using Currency Converter!")
        break

