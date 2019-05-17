


with open("info.txt") as f:
	lines = [l for l in f.readlines() if l.strip()][:4]

termmap = {
			"WinterSemester":"01", "WinterQuarter":"02",
			"SpringSemester":"03", "SpringQuarter":"04",
			"SummerSession1":"05", "SummerSpecialSession":"06",
			"SummerSession2":"07", "SummerQuarter":"08",
			"FallSemester":"09", "FallQuarter":"10"
			}

username = lines[0].strip().replace(" ","")
password = lines[1].strip().replace(" ","")
term = lines[2].strip().replace(" ","")
term = term[:4]+termmap[term[4:]]
CRNs = lines[3].strip().split(" ")
courses = [{"termCode":term, "course_number":x} for x in CRNs]

bas_url = "https://my.ucdavis.edu/schedulebuilder/"
# login url
login_url = "https://cas.ucdavis.edu/cas/login?service=https%3A%2F%2Fmy%2Eucdavis%2Eedu%2Fschedulebuilder%2Findex%2Ecfm%3Fsb"
url = bas_url+"index.cfm?termCode="+term+"&helpTour="

data = { 
		'password': password,
		'username': username,
		'submit': "LOGIN",
		'_eventId': 'submit'
		}