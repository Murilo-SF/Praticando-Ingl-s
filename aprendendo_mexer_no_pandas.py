import pandas as pd

data = pd.read_csv("data.csv")
data = pd.DataFrame(data)

print(data["traduction"])