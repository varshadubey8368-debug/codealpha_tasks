stock_prices = {"AAPL":180, "TSLA":250, "GOOGL":150, "AMZN":190, "MSFT":420}
total_investment = 0
print("=====Stock Portfolio Tracker=====")
while True:
    stock =  input("Enter stock name(or type 'done' to finish):").upper()
    
    if stock in stock_prices:
        quantity = int(input("Enter quantity:"))
        
        inverstment = stock_prices[stock]*quantity
        total_investment += inverstment
        print("Investment in", stock, "=", inverstment)
        
    else:
        print("Stock not found.Please enter a valid stock.")
        
print("\nTotal Investment Value =", total_investment)
print("Thank you!")