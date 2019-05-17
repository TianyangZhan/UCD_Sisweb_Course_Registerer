import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree
import json
import argparse
import time
import datetime

import config

parser = argparse.ArgumentParser()
parser.add_argument('--loop', '-l',action='store_true', help="do a infinity run of the script")
args = parser.parse_args()

with requests.Session() as session:
	# Log in
	r = session.get(config.url)
	soup = BeautifulSoup(r.content, "lxml")
	AUTH_TOKEN = soup.select_one("input[name=execution]")["value"]
	# update data, post and you are logged in.
	config.data["execution"] = AUTH_TOKEN
	r = session.post(config.login_url, data=config.data)

	curdate = int(datetime.datetime.today().weekday())
	curtime = int(time.strftime("%H%M%S"))
	
	while(len(config.courses) > 0):
		# Get class info
		site = session.get(config.url)
		for d in config.courses:
			r = session.post(config.bas_url+"course_search/course_search_results.cfm", data=d)
			result = r.json()
			unit = str(result["Results"]["DATA"][0][5])
			# Register
			if int(result["Results"]["DATA"][0][-3]) == 0:
				r = session.get(config.bas_url+"addCourseRegistration.cfm?Term="+d["termCode"]+"&CourseCRNs="+d["course_number"]+"&Schedule=Schedule%201&WaitlistedFlags=N&Units="+unit+"&ShowDebug=0")
				msg = r.json()
				if msg["Messages"]["DATA"][0][5] == "T": #msg["Messages"]["DATA"][0][3]
					config.courses[:] = [x for x in config.courses if x["course_number"] != d["course_number"]]
					print("Register Class "+d["course_number"]+" Successfully")
				else:
					print("Failed to Register Class "+d["course_number"])

		if len(config.courses) == 0:
			break
		if args.loop:
			break
		if (curdate <= 5 and curtime <= 200000) or (curdate > 5 and curtime <= 100000):
			break
		print("Try again in 2 seconds.")
		time.sleep(2)



