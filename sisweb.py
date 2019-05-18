import requests, json, argparse
from bs4 import BeautifulSoup
from xml.etree import ElementTree
import time, datetime,random

import config
from sendemail import send_email

parser = argparse.ArgumentParser()
parser.add_argument('--loop', '-l',action='store_true', help="do a infinity run of the script")
args = parser.parse_args()

with requests.Session() as session:

	r = session.get(config.url)
	soup = BeautifulSoup(r.content, "lxml")
	AUTH_TOKEN = soup.select_one("input[name=execution]")["value"]
	# update data, post and you are logged in.
	config.data["execution"] = AUTH_TOKEN
	r = session.post(config.login_url, data=config.data)
	
	while(len(config.courses) > 0):
		
		curdate = int(datetime.datetime.today().weekday())
		curtime = int(time.strftime("%H%M%S"))

		if (curdate <= 5 and curtime <= 200000) or (curdate > 5 and curtime <= 100000):
			print("Can not register. Not during Open Registration Hours")
			break
		
		# Get class info
		site = session.get(config.url)
		for d in config.courses:
			r = session.post(config.bas_url+"course_search/course_search_results.cfm", data=d)
			result = r.json()
			unit = str(result["Results"]["DATA"][0][5])
			course_title = str(result["Results"]["DATA"][0][22])+" "+str(result["Results"]["DATA"][0][3]+" "+str(result["Results"]["DATA"][0][23]))
			# Register
			if int(result["Results"]["DATA"][0][-3]) == 0:
				r = session.get(config.bas_url+"addCourseRegistration.cfm?Term="+d["termCode"]+"&CourseCRNs="+d["course_number"]+"&Schedule=Schedule%201&WaitlistedFlags=N&Units="+unit+"&ShowDebug=0")
				msg = r.json()
				try:
					if msg["Success"] != 1:
						print("Already Registered Class "+d["course_number"])
						config.courses[:] = [x for x in config.courses if x["course_number"] != d["course_number"]]
					elif msg["RegistrationStatusCodes"]["DATA"][0][0] == "Registered":
						config.courses[:] = [x for x in config.courses if x["course_number"] != d["course_number"]]
						email = config.data["username"]+"@ucdavis.edu"
						password = config.data["password"]
						header = "Auto Course Rigisterer Report"
						success_msg = "Successfully Registered Class "+d["course_number"]
						print(success_msg)
						send_email(email,password,email,header,"Dear "+config.data["username"]+",\n\nYou Have "+success_msg+" "+course_title+" at "+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
				except:
					print("Failed to Register Class "+d["course_number"])

		if len(config.courses) == 0:
			print("All classes are registered")
			break
		if not args.loop:
			break
		
		sleeptime = 30*random.randint(1,10)
		print("Try again in {0} seconds.".format(sleeptime))
		time.sleep(sleeptime)

