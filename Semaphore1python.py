import threading
import time

class Semaphore:
    def __init__(self, max_count):
        self.semaphore = threading.Semaphore(max_count)
    
    def acquire(self):
        self.semaphore.acquire()
    
    def release(self):
        self.semaphore.release()
        
def task(name, delay, semaphore):
    print(f"{name} is waiting to acquire the semaphore")
    semaphore.acquire()
    print(f"{name} acquired the semaphore")
    print(f"{name} started")
    time.sleep(delay)
    print(f"{name} completed")
    semaphore.release()
    print(f"{name} released the semaphore")

#Create a semaphore with a maximum of 2 concurrent tasks
semaphore = Semaphore(2)

#Create and start threads
threads = []
for i, delay in zip(range(1, 5), [2, 1, 3, 1.5]):
    thread = threading.Thread(target=task, args=(f"Task {i}", delay, semaphore))
    threads.append(thread)
    thread.start()

#Wait for all threads to complete
for thread in threads:
    thread.join()
    
#filename is Semahore1python
