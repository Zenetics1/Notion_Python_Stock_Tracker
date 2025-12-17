from twelvedata import TDClient
from dotenv import load_dotenv

load_dotenv()

import os
import requests

Twelve_Data_API_Key = os.getenv("TwelveData_API_Key")
Notion_Secret = os.getenv("Notion_Internal_Secret")