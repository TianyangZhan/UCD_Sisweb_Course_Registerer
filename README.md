# UCD_SISWEB_Course_Registerer

A simple python script to monitor available seats for courses on ucd sisweb.


Requirements: 

    Python 3.x
    
    pip install -r requirements.txt

Usage: 

  Single try:

    python sisweb.py
  
  Loop during (20:00-0:00,M-F; 10:00-0:00,Weekends)
    
    python sisweb.py --loop
    python sisweb.py -l


