import threading
import time

class Monitor:
	def __init__(self):
		self.mutex = threading.Lock()
		self.condition = threading.Condition(self.mutex)

	def synchronized(self, method):
		with self.condition:
			method()

def task(name, delay, monitor):
	def run_task():
		print(f"{name} entered monitor")
		print(f"{name} started")
		time.sleep(delay)
		print(f"{name} completed")
		print(f"{name} exited monitor")
	monitor.synchronized(run_task)

#Create a monitor
monitor = Monitor()

#Create and start threads
threads = []
for i, delay in zip(range(1, 5), [2, 1, 3, 1.5]):
	thread = threading.Thread(target = task, args=(f"Task {i}", delay, monitor))
	threads.append(thread)
	thread. start()

#Wait for all threads to complete
for thread in threads:
	thread.join()

#filename is Monitor1python
