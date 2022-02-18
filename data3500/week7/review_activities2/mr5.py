print("hello")

f = open("/home/ec2-user/environment/week7/zoomsession2/AAPL.txt", "r")
lines = f.readlines()
print("lines: ", lines)

prices = []
for line in lines:
    prices.append(round(float(line),2))
    
print("prices: ", prices)


i = 0
buy = 0
tot_profit = 0
first_buy = 0
for price in prices:
    if i >= 5: # 7 day moving average
        avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5] ) / 5
        # print("avg: ", avg)
        if price < avg * 0.95 and buy == 0:
            print("buying at: ", price)
            buy = price
            if first_buy == 0:
                first_buy = buy
                print("first buy: ", first_buy)
        elif price > avg * 1.05 and buy != 0:
            print("selling at: ", price)
            tot_profit += price - buy
            print("trade profit: ", round(price - buy,2))
            buy = 0
        else:
            pass #do nothing
        
    i += 1
print("---------------------------------")
print("tot_profit: ", round(tot_profit,2))
print("first buy: ", first_buy)
print("percentage returns: ", round((tot_profit/first_buy) * 100,2))