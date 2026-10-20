
# CodeAlpha Task 2: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420,
    "GOOGL": 170,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("\nAvailable stocks and prices:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price} per share")

print("\nEnter your stock details.")
print("Type 'done' when you finish.\n")

while True:
    stock = input("Enter stock name: ").strip().upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose an available stock.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid whole number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\n===== YOUR PORTFOLIO =====")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    total_investment += value

    print(
        f"{stock}: {quantity} shares x "
        f"${stock_prices[stock]} = ${value}"
    )

print(f"\nTotal investment value: ${total_investment}")

save = input("\nSave result to a text file? (yes/no): ").strip().lower()

if save == "yes":
    with open("portfolio_result.txt", "w") as file:
        file.write("STOCK PORTFOLIO TRACKER\n\n")

        for stock, quantity in portfolio.items():
            value = stock_prices[stock] * quantity
            file.write(
                f"{stock}: {quantity} shares = ${value}\n"
            )

        file.write(
            f"\nTotal investment value: ${total_investment}\n"
        )

    print("Result saved to portfolio_result.txt")

print("\nThank you for using Stock Portfolio Tracker!")
