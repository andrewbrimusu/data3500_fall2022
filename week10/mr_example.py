import json

# this example from week 7 has been updated to give an example of adding shorting logic
# please watch week14 zoom session2 for information on how to do this

# note: I named my variable "short", "sell" would be another great variable name you might want to use

        
def meanReversionStrategy(prices):
    i = 0
    buy = 0
    short = 0
    total_profit = 0
    for p in prices:
        if i >= 5: 
            moving_average = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
            
            #simple moving average logic, not mean
            if p < moving_average * .96 and buy == 0: #buy
                print("buying at: ", p)
                buy = p
                if short != 0 and buy != 0:
                    total_profit += short - buy
                    print("trade profit", short - buy)
                    print("total profit: ", total_profit)
                short = 0
            elif p > moving_average * 1.04 and short == 0: #sell, a sell signal is the same thing as a short signal
                short = p
                print("shorting at: ", p)
                if short != 0 and buy != 0:
                    total_profit += short - buy
                    print("trade profit", short - buy)
                    print("total profit: ", total_profit)
                buy = 0
        i += 1
        
    final_percentage = (total_profit / prices[0]) * 100
    print("total profit: ", total_profit)
    print("final percentage: ", final_percentage, "%")
    
    return total_profit, final_percentage



ticker = "aapl"

fil = open("/home/ubuntu/environment/week10/data/" + ticker + ".txt")
lines = fil.readlines()
# print(lines)

prices = []
for line in lines:
    prices.append(float(line))      
    
profit, returns = meanReversionStrategy(prices)

print(ticker, "profit: ", profit)
print(ticker, "returns: ", returns)
