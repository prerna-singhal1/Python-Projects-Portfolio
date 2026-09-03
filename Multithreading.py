import threading
import time

def walk_dog(first, last):
    time.sleep(4)
    print(f"Time to take {first} {last} for a walk!")
def do_coding():
    time.sleep(6)
    print("Time to do coding!")
def eat():
    time.sleep(4)
    print("Time to eat!")

chore_1 = threading.Thread(target=walk_dog, args= ("Wuff", "Tuff"))
chore_1.start()

chore_2 = threading.Thread(target=do_coding)
chore_2.start()

chore_3 = threading.Thread(target=eat)
chore_3.start()

chore_1.join()
chore_2.join()
chore_3.join()

print("All chores completed!")