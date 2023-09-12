import requests
import pandas as pd

api_url = 'https://reqres.in/api/users?page=2'

response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
    users = data.get('data', [])
    output_file = 'output.txt'
    df = pd.DataFrame(users)
    df['Name'] = df['first_name'] + df['last_name']
    df = df[['id', 'email', 'Name']]  # To select the necessary columns
    df.columns = ['Id', 'Email', 'Name']
    df.index = df.index + 1
    df.to_csv('output.txt', sep='\t', index=True)

    print(f'Data written to {output_file}')
else:
    print("Not found")
