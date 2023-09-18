from reader import *
from threading import Thread
from datetime import datetime
import global_
import socket
import time

debug = 0

def is_connected():
    try:
        # Attempt to resolve a common hostname
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

def getDatetime():
    return datetime.now().strftime("%m/%d/%Y %H:%M:%S")

##############################################################
# This acts as the main loop of the program, ran in a thread #
##############################################################

def myLoop():
    global reader
    global no_wifi_shown, no_wifi
    print("Now reading ID Card")
    last_tag = 0
    last_time = 0
    while True:
        time.sleep(0.1)
        in_waiting = reader.getSerInWaiting()
        tag = 0
        if in_waiting >= 14:
            if not is_connected():
                print("ERROR wifi is not connected")
            tag = reader.grabRFID()
            if tag == last_tag and not reader.canScanAgain(last_time):
                print("Suppressing repeat scan")
                continue

            s_reason = reader.checkRFID(tag)

            if s_reason != "good":
                print(s_reason)
                continue
            else:
                print("RFID Check Succeeded")
                
            global_.setRFID(tag)

            # Get a list of all users
            user_db = global_.user_db
            user_data = user_db.get_all_records(numericise_ignore=["all"])

            curr_user = "None"

            for i in user_data:
                if i["Card UUID"] == tag:
                    curr_user = i
            
            if curr_user == "None":
                print("User was not found in the database")
            else:
                new_row = [getDatetime(), int(time.time()), curr_user["Name"], str(tag), "User Checkin", "", "", ""]
                activity_log = global_.activity_log
                activity_log.append_row(new_row)

            last_time = time.time()
            last_tag = tag

            reader.readSerial()
    
if __name__ == "__main__":
    global_.init()
    global reader
    reader = Reader()
    myLoop()
    print("Starting thread")
    print("Made it to thread start")
