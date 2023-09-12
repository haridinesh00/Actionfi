import psycopg2
import requests
import pandas as pd

api_key = 'b0d82b3de51b87af4e4ea6263e03f4fa'

api_endpoint = 'http://api.weatherstack.com/current'
query_params = {
    'access_key': api_key,
    'query': 'Kozhikode',
}

db_settings = {
    'dbname': 'api_data',
    'user': 'postgres',
    'password': 'Iamsmall10',
    'host': 'localhost',
    'port': '5432'
}

try:
    response = requests.get(api_endpoint, params=query_params)

    if response.status_code == 200:
        data = response.json()
        current = data.get('current', [])
        df = pd.DataFrame([current])

        df.to_csv('api_data.txt', sep="\t", index=False)

    else:
        print(f'Error: {response.status_code} - {response.text}')

except requests.exceptions.RequestException as e:
    print(f'Error: {e}')
