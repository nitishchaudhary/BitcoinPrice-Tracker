from plyer import notification
import time
import requests
import json
alert_price = int(input("Enter the price for alert! :"))
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
check = True
clone_value = 0
while(True):
	response = requests.get(url = url)
	js = response.json()
	data = json.dumps(js)
	formatted_text = json.loads(data)
	Bitcoin_string= formatted_text["bpi"]["USD"]["rate"]
	Bitcoin_value = int(float(Bitcoin_string.replace(',','')))
	
	if clone_value != Bitcoin_value:
		print(f"Current Bitcoin Price is:\n {Bitcoin_value}")
	
	if ((Bitcoin_value < alert_price) and (check == True)):
		print("!LOW VALUE!")
		notification.notify(
			title = "Price Alert",
			message = f"Price: {Bitcoin_value}",	
			timeout = 5)
		check = False
	else:
		check = True
	clone_value = Bitcoin_value
	time.sleep(2)