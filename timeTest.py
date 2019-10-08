#!/usr/bin/python3

import hashlib
import time
import argparse
from multiprocessing import Process, Manager


#TODO 
# Run the Script using just arguments and time stamps 
#parser = argparse.ArgumentParser(description="Checks to see if a timestamp is being used to generate a hash.")
#parser.add_argument("hash", help='')
#parser.add_argument("start_time" help='')
#parser.add_argument("end_time" help='')
#args = parser.parse_args()


hashed = '8e52b3df6e8f53575e26231127d8ee8be24b6c3c'
startTime = 1570465620000
            
endTime = 1570465630000
          

start_run = time.time()

for i in range(startTime, endTime):
    if(hashlib.sha1(str(i).encode()).hexdigest() == hashed):
        print("hash " + hashlib.sha1(str(i).encode()).hexdigest() + "time " + i)

end_time = time.time()
total_time = end_time - start_run

print("end time " + str(total_time))
     
