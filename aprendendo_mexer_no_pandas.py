import pandas as pd

data = pd.read_csv("data.csv")
datas = pd.DataFrame(data)

print(datas["word"][1])
print(datas["traduction"][1])