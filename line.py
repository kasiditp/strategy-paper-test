import requests, json
import urllib
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
url = "https://notify-api.line.me/api/notify"
LINE_ACCESS_TOKEN = os.getenv("LINE_ACCESS_TOKEN")

class Line(object):
	@staticmethod
	def line_text(message):
		msg = urllib.parse.urlencode({"message": message})
		LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
		session = requests.Session()
		a=session.post(url, headers=LINE_HEADERS, data=msg)
		print(a.text)
