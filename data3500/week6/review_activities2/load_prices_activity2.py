file = open("/home/ec2-user/environment/week6/review_activities2/AAPL.txt")

# "/home/ubuntu/environment/hw4/AAPL.txt"

lines = file.readlines()

print(lines)

prices = []
for line in lines:
    prices.append(float(line))
    
print(prices)

