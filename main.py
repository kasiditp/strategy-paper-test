from line import Line
import json
import requests
import threading

noti_line = Line()

def printit():
  threading.Timer(300, printit).start()
  response = requests.get('http://localhost:5000/percunia/5min/usdt-eth')
  if response.status_code == 200:
    if json.loads(response.content.decode('utf-8'))['value']:
      print('Signal found')
      noti_line.line_text('signal found')
    else:
      print('Signal not found')
      noti_line.line_text('signal not found')
  else:
    print('Fail')

if __name__ == "__main__":
  printit()