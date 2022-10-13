import pymssql
import time

conn = pymssql.connect(host='reathema10.database.windows.net', port=1433,
database='Thema10', user='kw1c@reathema10.database.windows.net', password='P@ssword')

import RPi.GPIO as GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True: 
    if GPIO.input(10) == GPIO.HIGH:
        cur = conn.cursor()
        timestamp = int( time.time() )
        cur.execute("INSERT INTO Oefening21MaxJimmy VALUES('Button', 'Pressed', " + str(timestamp) +")")
        print("Je klik is verstuurd naar de database met timestamp " + str(timestamp))
        conn.commit()
        time.sleep(2)
        
 
conn.close()


