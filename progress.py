import time

def show_progress():
    while True:
        print("Processing...", end="\r")
        time.sleep(1)
