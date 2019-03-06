from line import Line
import json
import requests
import threading

noti_line = Line()

coins = ['usdt-eth', 'usdt-xrp', 'usdt-btc', 'usdt-bch', 'usdt-etc', 'usdt-trx', 'usdt-ltc', 'usdt-neo', 'usdt-xmr']

def printit():
  threading.Timer(300, printit).start()
  for coin in coins:
    response = requests.get('http://localhost:5000/percunia/5min/' + coin)
    if response.status_code == 200:
      if json.loads(response.content.decode('utf-8'))['value']:
        print('Signal found: ', coin)
        noti_line.line_text('signal found: ' + coin)
      else:
        print('Signal not found: ', coin)
    else:
      print('Fail')

if __name__ == "__main__":
  printit()