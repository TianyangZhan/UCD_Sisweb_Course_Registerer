# UCD_SISWEB_Course_Registerer

A simple python script to monitor available seats for courses on ucd sisweb during open registration.


Requirements: 

    Python 3.x
    
    pip install -r requirements.txt

Usage: 

  *Input your login and class information in info.txt

  Single run:

    python sisweb.py
  
  Loop during (20:00-0:00,M-F; 10:00-0:00,Weekends)
    
    python sisweb.py --loop
    python sisweb.py -l

Email Settings:
    
   You will get an email from your own ucd email account.
   
   Possible error when sending email:
   
    smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8 http://support.google.com/mail/bin/answer.py?answer=14257\n5.7.8 {BADCREDENTIALS} s10sm9426107qam.7 - gsmtp')
   
   Solution:
   
        1. Log in to your ucd email
        2. Go to https://www.google.com/settings/security/lesssecureapps and allow less secure apps access


