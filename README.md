# UCD_SISWEB_Course_Registerer

A simple python script to monitor available seats for courses on ucd sisweb during open registration.


Requirements: 

    Python 3.x
    
    pip install -r requirements.txt

Usage: 

  *Input your login and class information in info.txt

  Single run:

    python sisweb.py
  
  Loop run during (20:00-0:00, M-F;  10:00-0:00, Weekends)
    
    python sisweb.py --loop
    python sisweb.py -l

Email Settings:
    
   You will get an email from your own ucd email account.
   
   Possible error when sending email:
   
 (535, b'5.7.8 Username and Password not accepted.)
   
   Solution:
   
 1. Log in to your ucd email
 2. Go to [Google Account Settings](https://www.google.com/settings/security/lesssecureapps) and allow less secure apps access


