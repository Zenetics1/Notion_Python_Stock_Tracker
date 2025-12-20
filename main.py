from twelvedata import TDClient
from dotenv import load_dotenv

load_dotenv()

import os
import requests

"""Initialize Notion & Twelve Data API Keys from .env file"""
Twelve_Data_API_Key = os.getenv("TwelveData_API_Key")
Notion_Secret = os.getenv("Notion_Internal_Secret")

"""Notion API POST Request component setup"""
header = {
    "Authorization": f"Bearer {Notion_Secret}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

Notion_DB_ID = "2cca3154e95980aa9118ff6cc25e4065"
Notion_DB_URL = f"https://api.notion.com/v1/databases/{Notion_DB_ID}/query"

"""Initial Test for inputting stock symbol and retrieving price data from Twelve Data API"""
td = TDClient(apikey=Twelve_Data_API_Key)

response = requests.post(Notion_DB_URL, headers=header)

DB_Query = response.json()

for page in DB_Query['results']:
    if page['properties']['Status']['status']['name'] == 'Add Stock':

        page_id = page['id']

        stock_symbol = page['properties']['Symbol']['rich_text'][0]['text']['content']
        selected_stock = td.quote(symbol=stock_symbol).as_json()

        selected_stock_name = selected_stock['name']
        selected_stock_price_high = selected_stock['high']

        Notion_Page_Endpoint = f"https://api.notion.com/v1/pages/{page_id}"

        payload = {
            "properties":{
                "Symbol": {
                    "rich_text": [
                        {
                            "text": {
                                "content": stock_symbol
                            }
                        }
                    ]
                },
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": selected_stock_name
                            }
                        }
                    ]
                },
                "Price High":{
                    "number": float(selected_stock_price_high)
                },
                "Status": {
                    "status": {
                        "name": "Continuously Update"
                    }
                }
            }
        }
        response = requests.patch(Notion_Page_Endpoint, headers=header, json=payload)
        print(response.status_code)
        print(response.json())
    elif page['properties']['Status']['status']['name'] == "Continuously Update":

        page_id = page['id']

        stock_symbol = page['properties']['Symbol']['rich_text'][0]['text']['content']
        
        selected_stock = td.quote(symbol=stock_symbol).as_json()
        selected_stock_price_high = selected_stock['high']

        Notion_Page_Endpoint = f"https://api.notion.com/v1/pages/{page_id}"

        payload = {
            "properties":{
                "Price High":{
                    "number": float(selected_stock_price_high)
                }
            }
        }

        response = requests.patch(Notion_Page_Endpoint, headers=header, json=payload)
        print(response.status_code)
        print(response.json())

