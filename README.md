Script written in Python to track stocks and other investment opportunities through a Notion webpage. 

Utilizes Twelve Data and Notion API, querying a Notion database table for user added stock symbols and then accessing metrics related to said stock. Gathered information is then formatted and added to the database as a new Notion page. 

Script will run periodically, updating the metrics for existing stocks in the database and adding any newly added stock symbols. This is done by checking the stocks status on the table, which is either, "Add Stock", "Continously Update", or "Stop Tracking".

Current displayed data includes: Stock Symbol, Company Name, Price, Low Price, High Price, Volume, and Change in Stock Price.
