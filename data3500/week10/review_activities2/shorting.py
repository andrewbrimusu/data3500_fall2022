print("hello")

f = open("/home/ec2-user/environment/week10/zoomsession2/GOOG.txt", "r")
lines = f.readlines()
print("lines: ", lines)

prices = []
for line in lines:
    prices.append(float(line))
    
print("prices: ", prices)


# simple moving average crossover strategy, 5 day moving average
i = 0
buy = 0
sell = 0
position = 0
tot_profit = 0
for price in prices:
    if i >= 5: # 5 day moving average
        avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5] ) / 5
        # print("avg: ", avg)
        if price > avg and position != 1:
            buy = price
            print("buying at: ", price)
            if buy != 0 and sell != 0:
                tot_profit += sell - buy
                print("trade profit: ", price - buy)
            position = 1
        elif price < avg and position != -1:
            sell = price
            print("selling at: ", price)
            if buy !=0 and sell != 0:
                tot_profit += sell - buy
                print("trade profit: ", price - buy)
            position = -1
        else:
            pass #do nothing
        
    i += 1
print("tot_profit: ", tot_profit)
print("annual returns: ", tot_profit/prices[0])

# call the function down here