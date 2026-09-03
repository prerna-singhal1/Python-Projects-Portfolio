import time

def count(stop, start=0):
    for x in range(start, stop+1):
        print(x)
        time.sleep(1.5)
    print("DONE!")

count(3, 1)