import pandas as pd
import plotly.express as px
import requests

url = "https://www.forbes.com/forbesapi/person/billionaires/2023/position/true.json?filter=finalWorth,age,country,qas,rank,category,person,personName,organization,gender,squareImage"
print(requests.get(url).status_code)
resp = requests.get(url).json()['personList']['personsLists']


df = pd.DataFrame.from_dict(resp)
df['birthDate'] = pd.to_datetime(df['birthDate'], unit='ms').dt.date
df["finalWorth"] = df["finalWorth"].apply(
    lambda x: x * 10 ** 6)  # converting to USD

sz = df['finalWorth'].size-1
df['Percentile'] = df['finalWorth'].rank(
    method='max').apply(lambda x: round(100.0 * (x - 1) / sz, 3))

fig = px.scatter(df, x="birthDate", y="finalWorth",
                 color="gender", hover_data=['uri'],
                 marginal_x="histogram", marginal_y="violin",
                 title="Date of Birth v. Net Worth",
                 labels={
                     "birthDate": "Date of Birth",
                     "finalWorth": "Net Worth (in USD)",
                     "gender": "Gender"
                 },)

fig.write_image("scatter.png", height=1080, width=1920, scale=3)

df.to_csv("billionaires.csv", encoding='utf-8', index=False)
