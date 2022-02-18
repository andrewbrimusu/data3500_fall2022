import json
print("hello")

f = open("/home/ec2-user/environment/week10/zoomsession2/GOOG.txt", "r")
lines = f.readlines()
print("lines: ", lines)

prices = []
for line in lines:
    prices.append(float(line))
    
print("prices: ", prices)


def simpleMovingAverageStrategy(prices):
    i = 0
    buy = 0
    tot_profit = 0
    first_buy = 0
    for price in prices:
        if i >= 5: # 5 day moving average
            avg = ( prices[i-1] + prices[i-2] + prices[i-3] + prices[i-4] + prices[i-5] ) / 5
            # print("avg: ", avg)
            if price > avg and buy == 0:
                print("buying at: ", price)
                buy = price
                if first_buy == 0:
                    first_buy = price
            elif price < avg and buy != 0:
                print("selling at: ", price)
                tot_profit += price - buy
                print("trade profit: ", price - buy)
                buy = 0
            else:
                pass #do nothing
            
        i += 1
    returns = (tot_profit / first_buy) * 100
    print("tot_profit: ", tot_profit)
    print("returns: ", returns)

    return tot_profit, returns
    
prof, returns = simpleMovingAverageStrategy(prices)

profit_dictonary = {}
profit_dictonary["profit"] = prof
profit_dictonary["returns"] = returns

json.dump(profit_dictonary, open("/home/ec2-user/environment/week10/zoomsession2/results.json", "w"))

# call the function down here