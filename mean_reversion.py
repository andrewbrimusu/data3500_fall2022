file = open("/home/ubuntu/environment/tsla.txt")
lines = file.readlines()
print(lines)

prices = []
for line in lines:
    prices.append(float(line))
print(prices)


buy = 0.0
profit = 0.0
i = 0

for price in prices:
    if i >= 5:
        avg = (prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5]) / 5
        if price > avg and buy == 0.0: # buy
            buy = price
        elif price < avg and buy != 0.0: # sell
            profit += price - buy
            buy = 0.0
            
    i += 1
        
print("profit: ", profit)
print("returns: ", profit/prices[0])

