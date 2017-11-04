#!/usr/bin/env python

import websocket
import json
import time
import sys

price_factor = float(1e5)
amount_factor = float(1e8)

ws = websocket.WebSocket()
ws.connect("wss://api.bl3p.eu/1/BTCEUR/orderbook")

#{"asks":[{"price_int":504621000,"amount_int":252500000},{"price_int":504923000,"amount_int":147500000},{"price_int":505000000,"amount_int":20486543},{"price_int":505085000,"amount_int":630100000},{"price_int":505871000,"amount_int":100000000},{"price_int":506430000,"amount_int":459200000},{"price_int":506434000,"amount_int":372100000},{"price_int":507341000,"amount_int":500000000},{"price_int":507737000,"amount_int":125000000},{"price_int":508750999,"amount_int":121073509},{"price_int":508751000,"amount_int":438213658},{"price_int":509100000,"amount_int":48171540},{"price_int":509644000,"amount_int":10000000},{"price_int":510000000,"amount_int":62640384},{"price_int":510101010,"amount_int":198000000},{"price_int":510127238,"amount_int":9874609},{"price_int":510766000,"amount_int":1378572816},{"price_int":511427999,"amount_int":198953283},{"price_int":511500000,"amount_int":32541637},{"price_int":511551150,"amount_int":164549990},{"price_int":512500000,"amount_int":210804866},{"price_int":514645981,"amount_int":19821},{"price_int":514800000,"amount_int":14732973},{"price_int":514900000,"amount_int":816993595},{"price_int":515000000,"amount_int":239067343},{"price_int":515606340,"amount_int":19588},{"price_int":516130000,"amount_int":20000000},{"price_int":516500000,"amount_int":3411710},{"price_int":517676000,"amount_int":400000000},{"price_int":517844000,"amount_int":10000000}],"bids":[{"price_int":501331000,"amount_int":100000000},{"price_int":500345000,"amount_int":500000000},{"price_int":499332000,"amount_int":125000000},{"price_int":499168999,"amount_int":49999999},{"price_int":498332000,"amount_int":875000000},{"price_int":498320000,"amount_int":44000000},{"price_int":497982000,"amount_int":350000000},{"price_int":497629000,"amount_int":1500000000},{"price_int":497000000,"amount_int":41356338},{"price_int":495000001,"amount_int":120303493},{"price_int":495000000,"amount_int":496107901},{"price_int":493963000,"amount_int":1200000000},{"price_int":490100000,"amount_int":164544174},{"price_int":490000000,"amount_int":10000000},{"price_int":485000000,"amount_int":12038350},{"price_int":484000000,"amount_int":413223},{"price_int":482100000,"amount_int":64414554},{"price_int":480100000,"amount_int":2603624},{"price_int":480000000,"amount_int":47055207},{"price_int":477500000,"amount_int":408376},{"price_int":476000000,"amount_int":16796218},{"price_int":475800000,"amount_int":100000000},{"price_int":475133273,"amount_int":292271680},{"price_int":475000000,"amount_int":79657675},{"price_int":471463643,"amount_int":1396508719},{"price_int":471000000,"amount_int":7420382},{"price_int":470300000,"amount_int":52231979},{"price_int":470200000,"amount_int":10633772},{"price_int":470125000,"amount_int":6344057},{"price_int":470100000,"amount_int":2659008}]}

def print_values(positions):
	ret = ""
	amount_cum = 0.0
	for position in positions:
		price_int = position["price_int"]
		amount_int = position["amount_int"]
		price = float(price_int) / price_factor
		amount = float(amount_int) / amount_factor
		amount_cum += amount
		ret += "%d,%f,%f,%f\n" % (now, price, amount, amount_cum)
	return ret


while True:
	json_str = ws.recv()
	now = int(time.time())
	orderbook = json.loads(json_str)
	asks = orderbook["asks"]
	bids = orderbook["bids"]
	
	print >> sys.stdout, print_values(asks)
	print >> sys.stderr, print_values(bids)
	sys.stdout.flush()
	sys.stderr.flush()
