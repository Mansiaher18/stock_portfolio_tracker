import csv
import os

FILE_NAME = "stocks.csv"


def load_stocks():
    stocks = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                row["quantity"] = int(row["quantity"])
                row["buy_price"] = float(row["buy_price"])
                row["current_price"] = float(row["current_price"])
                stocks.append(row)

    return stocks


def save_stocks(stocks):
    with open(FILE_NAME, "w", newline="") as file:
        fields = [
            "name", "quantity", "buy_price", "current_price"
        ]

        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(stocks)


portfolio = load_stocks()

while True:
    print("\n--- Stock Portfolio Tracker ---")
    print("1. Add Stock")
    print("2. View Portfolio")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter stock name: ").upper()

        try:
            quantity = int(input("Enter quantity: "))
            buy_price = float(input("Enter purchase price per share: "))
            current_price = float(input("Enter current price per share: "))

            if quantity <= 0 or buy_price < 0 or current_price < 0:
                print("Enter valid values.")
                continue

            stock = {
                "name": name,
                "quantity": quantity,
                "buy_price": buy_price,
                "current_price": current_price
            }

            portfolio.append(stock)
            save_stocks(portfolio)

            print("Stock added and saved successfully!")

        except ValueError:
            print("Please enter valid numeric values.")

    elif choice == "2":
        if not portfolio:
            print("Portfolio is empty.")
            continue

        total_investment = 0
        total_current_value = 0

        for stock in portfolio:
            investment = stock["quantity"] * stock["buy_price"]
            current_value = stock["quantity"] * stock["current_price"]
            profit_loss = current_value - investment

            total_investment += investment
            total_current_value += current_value

            print(f"\nStock: {stock['name']}")
            print(f"Investment: Rs. {investment:.2f}")
            print(f"Current Value: Rs. {current_value:.2f}")
            print(f"Profit/Loss: Rs. {profit_loss:.2f}")

        print("\n--- Portfolio Summary ---")
        print(f"Total Investment: Rs. {total_investment:.2f}")
        print(f"Current Value: Rs. {total_current_value:.2f}")
        print(f"Total Profit/Loss: Rs. {total_current_value - total_investment:.2f}")

    elif choice == "3":
        print("Thank you for using Stock Portfolio Tracker!")
        break

    else:
        print("Invalid choice. Enter 1, 2, or 3.")

