# import os
# os.system("pip3 install pandas")

import pandas
df = pandas.read_csv("/home/ec2-user/environment/week11/content_videos/BA.csv")

print(df.keys())

print(df["Adj Close"])

for price in df["Adj Close"]:
    print(price)
    

#print(df.head())

# no checkpoint activity - I am not going to make you use pandas
# but give it a try, its very useful.




