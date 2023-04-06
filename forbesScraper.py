import pandas as pd
import plotly.express as px
import requests

url = "https://www.forbes.com/forbesapi/person/rtb/0/-estWorthPrev/true.json"
resp = requests.get(url).json()['personList']['personsLists']


df = pd.DataFrame.from_dict(resp)
df['birthDate'] = pd.to_datetime(df['birthDate'], unit='ms')
df["finalWorth"] = df["finalWorth"].apply(
    lambda x: x * 10 ** 6)  # converting to USD

sz = df['finalWorth'].size-1
df['Percentile'] = df['finalWorth'].rank(
    method='max').apply(lambda x: 100.0 * (x - 1) / sz)

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
