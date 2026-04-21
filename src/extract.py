import requests
from config import URL, ID_TOKEN, LIMIT

headers = {
    "X-App-Token": ID_TOKEN
}

def fetch_data(where_clause):

    offset = 0
    all_data = []

    while True:
        params = {
            "$where": where_clause,
            "$limit": LIMIT,
            "$offset": offset
        }

        response = requests.get(URL, headers=headers, params=params)
        data = response.json()

        if not data:
            break
        
        all_data.extend(data)
        offset += LIMIT

        print(f"Descargados: {len(all_data)}")

    return all_data
