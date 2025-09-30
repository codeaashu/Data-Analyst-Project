import pandas as pd
df = pd.read_csv("EcommRawData.csv")
analyzeDf = df.drop_duplicates()
final_output = pd.DataFrame(analyzeDf.dropna())
final_output.to_csv("EcommFilterData.csv")