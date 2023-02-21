from datetime import datetime

def log_msg(message):
    print (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message)