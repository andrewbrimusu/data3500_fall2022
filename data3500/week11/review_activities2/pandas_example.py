import os
os.system("sudo pip3 install pandas")

import pandas

df = pandas.read_csv("/home/ec2-user/environment/week11/zoomsession2/ADBE.csv")

print(df["Adj Close"])

for price in df["Adj Close"]:
    print(price)

df.to_csv("df.csv")
print(df.head())