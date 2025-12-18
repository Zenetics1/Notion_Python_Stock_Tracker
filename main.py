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

Notion_New_Page_Endpoint = "https://api.notion.com/v1/pages"
Notion_DB_ID = "2cca3154e95980aa9118ff6cc25e4065"

"""Initial Test for inputting stock symbol and retrieving price data from Twelve Data API"""
td = TDClient(apikey=Twelve_Data_API_Key)
stock_symbol = input("Pick a stock symbol: ")
tst = td.price(symbol=stock_symbol).as_json()

"""Payload Test with Twelve Data API price data"""
payload = {
    "parent":{
        "database_id": Notion_DB_ID
    },
    "properties":{
        "Name": {
            "title": [
                {
                    "text": {
                        "content": "Test Stock"
                    }
                }
            ]
        },
        "Ticker": {
            "rich_text": [
                {
                    "text": {
                        "content": stock_symbol
                    }
                }
            ]
        },
        "Price":{
            "number": float(tst['price'])
        }
    }
}

response = requests.post(Notion_New_Page_Endpoint, headers=header, json=payload)

print(response.status_code)
print(response.json())

page_id = response.json()




