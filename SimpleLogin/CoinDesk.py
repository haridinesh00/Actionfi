import requests
import pandas as pd

api_url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"

response = requests.get(api_url)
json_data = response.json()
data = json_data.get('data', [])
# print(json_data)
df = pd.DataFrame(data)
df = df[['ID Nation', 'Nation', 'Year']]
print(df)
df.to_csv('coindesk.txt', sep="\t", index=True)
