file = open("/home/ec2-user/environment/week6/zoomsession2/AAPL.txt", "r")
lines = file.readlines()

prices = []
for line in lines: # converting lines to floats in a new list "prices"
    prices.append(float(line))
    
avg = (prices[0] + prices[1] + prices[2] + prices[3] + prices[4]) / 5
print("average first 5 prices: ", avg)
