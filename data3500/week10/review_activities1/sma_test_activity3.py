print("hello")

f = open("/home/ubuntu/environment/simplemovingaverage/GOOG.txt", "r")
lines = f.readlines()
print("lines: ", lines)

prices = []
for line in lines:
    prices.append(float(line))
    
print("prices: ", prices)



i = 0
buy = 0
tot_profit = 0
for price in prices:
    if i >= 5: # 7 day moving average
        avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5] ) / 5
        # print("avg: ", avg)
        if price > avg and buy == 0:
            print("buying at: ", price)
            buy = price
        elif price < avg and buy != 0:
            print("selling at: ", price)
            tot_profit += price - buy
            print("trade profit: ", price - buy)
            buy = 0
        else:
            pass #do nothing
        
    i += 1
print("tot_profit: ", tot_profit)

# call the function down here