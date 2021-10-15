from plyer import notification
import time
import requests
import json
import smtplib
from email.message import EmailMessage
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
		email_message = ""
		email = EmailMessage()
		email["from"] = "Bitcoin-Notifier"
		email["to"] = "006nschaudhary006@gmail.com"
		email["subject"] = "!Bitcoin Price drop!"
		email.set_content(email_message)

		#setting up username and password for gmail account
		email_id = "ncnitish6250@gmail.com"
		password = " "

		#initializing smtp server
		with smtplib.SMTP(host = "smtp.gmail.com" , port = 587) as smtp:
			smtp.ehlo()
			#connecting securely to the server
			smtp.starttls()
			smtp.login(email_id , password)
			smtp.send_message(email)

		check = False
	else:
		check = True
	clone_value = Bitcoin_value
	time.sleep(2)
