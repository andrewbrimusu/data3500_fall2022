# web json api

import numpy as np
import requests
import json
import time

url = "https://api.datamuse.com/words?rel_trg=cow"

req1 = requests.get(url)
# time.sleep(12)
print("req1: ", req1)

dct1 = json.loads(req1.text)

key1 = "word"
key2 = "score"


for item in dct1:
    # print(item)
    if item[key1] == "dairy":
        print(item[key2])
        
        
    
    
# print(dct1)

# key1 = "word"
# key2 = "score"
