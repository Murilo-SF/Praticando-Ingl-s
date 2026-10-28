import pandas as pd
from random import randint
data = pd.read_csv("data.csv")
inf = str(data["traduction"][32])
# print(len(data))
print(inf)
# if len(data) == 0:
    # print("AHAAM")