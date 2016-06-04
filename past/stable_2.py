import threading
from queue import Queue

class threadingOperation:
    dest=False #holds a pointer to function to be multithreaded.
    thCount=1 #specifies number of threads to be created
    myQueue=False
    results=[] #holds results of threading
    outputType="" #stores type of results, could be list or dict
    def __init__(self,*args):
        if len(args)<2:
            raise ValueError
        destFunc=args[0]
        thCount=args[1]
        self.dest=destFunc
        self.thCount=thCount
        if len(args)>2:
            if args[2]=="list":
                self.outputType="list"
            if args[2]=="dict":
                self.outputType="dict"
    def worker(self): #one worker per thread, each one will work until all tasks done, then dies
        if self.outputType=="":
            while True:
                self.dest( self.myQueue.get() ) #passes task to multied function
                self.myQueue.task_done() #signals to queue that particular task is finished
        elif self.outputType=="list":
            while True:
                self.results.append( self.dest( self.myQueue.get() ) ) #passes task to multied function
                self.myQueue.task_done() #signals to queue that particular task is finished
        elif self.outputType=="dict":
            while True:
                key=self.myQueue.get()
                self.results[key]=self.dest( key ) #passes task to multied function
                self.myQueue.task_done() #signals to queue that particular task is finished
    def thread(self,taskList):
        #taskList is a list of stuff
        #each element of the list is passed to an instance of the function
        #named in dest
        if self.outputType=="list":
            self.results=[]
        elif self.outputType=="dict":
            self.results=dict()
        self.myQueue=Queue() #make queue
        for i in range(self.thCount):
            t=threading.Thread(target=self.worker)
            t.daemon=True
            t.start()
        for x in taskList:
            self.myQueue.put(x)
        self.myQueue.join()
        if self.outputType!="":
            return self.results
