# File Name learn_threading_sync_queue.py
# Demo of python based threading
# link : https://www.tutorialspoint.com/python3/python_multithreading.htm
#!usr/bin/python3

from utility import *
printDes("Threading", """ Python threading: Synchronization and queue""")

import queue
import threading
import time

exitFlag = 0
sleepTime = [1, 0.5, 0.6]
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("Starting " + self.name)
        process_data(self.name, self.q, self.threadID - 1)
        print ("Exiting " + self.name)

def process_data(threadName, q, index):
    while not exitFlag:
        print("index : ", index)
        sleep = sleepTime[index]
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
            time.sleep(sleep)
        else:
            queueLock.release()
            print("%s empty queue:" % threadName,"and sleep time: ", sleep)
            time.sleep(sleep)
    if exitFlag == 1:
        print("Thread: ", threading.currentThread().getName(), " will exit")

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Create new threads
for tName in threadList:
   thread = myThread(threadID, tName, workQueue)
   thread.start()
   threads.append(thread)
   threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    print("Main Thread- Putting word: ", word)
    workQueue.put(word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
