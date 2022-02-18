file = open("/home/ec2-user/environment/week6/zoomsession2/AAPL.txt", "r")
lines = file.readlines()
tot = 0
avg = 0
for line in lines:
    price = float(line)
    tot += price
avg = tot / len(lines)
print("average: ", avg)
    