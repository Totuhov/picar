import threading
import time

def thread1_function(start_event, stop_event):
    start_event.wait()

    for i in range(6):
        time.sleep(1)
        print(f"Thread 1: {i}")

    stop_event.set()

def thread2_function(stop_event):
    while not stop_event.is_set():
        time.sleep(1)
        print("Thread 2: Still running")

    print("Thread 2: Stopping")

start_event = threading.Event()
stop_event = threading.Event()

thread1 = threading.Thread(target=thread1_function, args=(start_event, stop_event))
thread2 = threading.Thread(target=thread2_function, args=(stop_event,))

thread1.start()
thread2.start()

start_event.set()

thread1.join()
thread2.join()


print("Beide Threads haben beendet.")