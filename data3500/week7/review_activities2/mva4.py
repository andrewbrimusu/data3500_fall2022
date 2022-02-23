print("hello")

f = open("/home/ubuntu/environment/data3500/week7/review_activities2/GOOG.txt", "r")
lines = f.readlines()
print("lines: ", lines)

prices = []
for line in lines:
    prices.append(float(line))
    
print("prices: ", prices)


i = 0
buy = 0
for price in prices:
    if i >= 4: # 4 day moving average
        avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] ) / 4
        # print("avg: ", avg)
        if price > avg and buy == 0:
            print("buying at: ", price)
            buy = price
        elif price < avg and buy != 0:
            print("selling at: ", price)
            print("trade profit: ", price - buy)
            buy = 0
        else:
            pass #do nothing
        
    i += 1