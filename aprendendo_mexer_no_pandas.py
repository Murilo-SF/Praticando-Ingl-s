import pandas as pd

data = pd.read_csv("data.csv")
datas = pd.DataFrame(data)
inf = str(datas["traduction"][41])
inf = list(inf.split(";"))
resposta = input("Principalmente")
print(len(inf))
print(inf)
if resposta in inf:
    print("AHAM")