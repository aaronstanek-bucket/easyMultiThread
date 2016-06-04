def ImAFunction(x):
    return x**2

m=[6,7,2,3] #it's a list
w0=threadingOperation(ImAFunction,2)
#w0 is now a thingie that will create 2 threads and returns nothing


wl=threadingOperation(ImAFunction,3,"list")
#wl is now a thingie that will create 3 threads
wl.thread(m)
#this will return [36,49,4,9], but the elements may not be in that order

wd=threadingOperation(ImAFunction,4,"dict")
#wd is now a thingie that will create 4 threads that run ImAFunction
wd.thread(m)
#this will create a dictionary of the following
# {6: 36 , 7: 49 , 2: 4 , 3: 9}
