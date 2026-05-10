def investment():
    prices={
        "AAPL":380,
        "MSFT":400,
        "AMZN":350,
        "NVDA":320,
        "GOOGL":400,
        "META":360,
        "INFY":350
    }
    total=0
    n=int(input("how many stocks:"))
    for i in range(n):
        stock_name = input("enter stock name :").upper()
        if stock_name in prices:
            quantity=int(input("enter quantity:"))
            total+=prices[stock_name]*quantity
        else:
            print("invalid stock")
    print("total investiment is :",total)
    file = open("investment.txt", "w")
    file.write(f"Total investment is: {total}")
    file.close()

investment()



