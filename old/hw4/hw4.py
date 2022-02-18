file = open("/home/ubuntu/environment/hw4/AAPL.txt")

lines = file.readlines()

print(lines)

prices = []
for line in lines:
    prices.append(float(line))
    
print(prices)

tot = 0
i = 0
for price in prices:
    tot += price
    i += 1
print("avg: ", tot / i)

print("5 day avg: ", (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5)