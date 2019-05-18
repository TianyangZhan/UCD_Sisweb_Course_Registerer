import smtplib,time
from email.mime.text import MIMEText

import config


def send_email(owner,password,target,subject='Hello',message="Hello World"):
	try:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(owner,password)
		
		#Send the mail
		msg = MIMEText(message, 'plain')
		msg['From'] = owner
		msg['To'] = target
		msg['Subject'] = subject

		server.sendmail(owner, target, msg.as_string())
	except:
		print("Error Occured When Sending Email")



if __name__ == '__main__':
	email = config.data["username"]+"@ucdavis.edu"
	password = config.data["password"]
	send_email(email,password,email)