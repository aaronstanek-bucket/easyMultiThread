import threading
from queue import Queue
##import time

### lock to serialize console output
##lock = threading.Lock()
##
##def do_work(item):
##    time.sleep(.1) # pretend to do some lengthy work.
##    # Make sure the whole print completes or threads can mix up output in one line.
##    with lock:
##        print(threading.current_thread().name,item)
##
### The worker thread pulls an item from the queue and processes it
##def worker():
##    while True:
##        item = q.get()
##        do_work(item)
##        q.task_done()
##
### Create the queue and thread pool.
##q = Queue()
##for i in range(4):
##     t = threading.Thread(target=worker)
##     t.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
##     t.start()
##
### stuff work items on the queue (in this case, just a number).
##start = time.perf_counter()
##for item in range(20):
##    q.put(item)
##
##q.join()       # block until all tasks are done
##
### "Work" took .1 seconds per task.
### 20 tasks serially would be 2 seconds.
### With 4 threads should be about .5 seconds (contrived because non-CPU intensive "work")
##print('time:',time.perf_counter() - start)


class threadingOperation:
    dest=False #holds a pointer to function to be multithreaded.
    thCount=1 #specifies number of threads to be created
    myQueue=False
    def __init__(self,destFunc,thCount):
        self.dest=destFunc
        self.thCount=thCount
    def worker(self): #one worker per thread, each one will work until all tasks done, then dies
        while True:
            self.dest( self.myQueue.get() ) #passes task to multied function
            self.myQueue.task_done() #signals to queue that particular task is finished
    def thread(self,taskList):
        #taskList is a list of stuff
        #each element of the list is passed to an instance of the function
        #named in dest
        self.myQueue=Queue() #make queue
        for i in range(self.thCount):
            t=threading.Thread(target=self.worker)
            t.daemon=True
            t.start()
        for x in taskList:
            self.myQueue.put(x)
        self.myQueue.join()
