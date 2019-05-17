
username = "NAME"
password = "PASS"
term = "201910"
courses = [
			{"termCode":term, "course_number":"40344"}
		 ]
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