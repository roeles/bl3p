#!/usr/bin/env python

import websocket
import json
import time
import sys

price_factor = float(1e5)
amount_factor = float(1e8)

ws = websocket.WebSocket()
ws.connect("wss://api.bl3p.eu/1/BTCEUR/trades")

#{"date":1509098234,"price_int":509368999,"amount_int":20000000}


while True:
	json_str = ws.recv()
	trade = json.loads(json_str)
	now = int(time.time())
	date = trade["date"]
	price_int = trade["price_int"]	
	amount_int = trade["amount_int"]
	price = float(price_int) / price_factor
	amount = float(amount_int) / amount_factor
	print "%d,%d,%f,%f" % (now, date, price, amount)
	sys.stdout.flush()
