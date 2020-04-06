import pandas as pd

df = pd.read_json("./sample.json")
print(df)

df.to_csv("./csv/sample.csv")
print("script end successfully")
