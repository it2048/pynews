__author__ = 'it2048'

import urllib2
import socket
import re
import threading
socket.setdefaulttimeout(3)
THN = 50 #Thread namount
FLC = 5 #The store file number
PTH = 'E:/ip/ip'
class myThread (threading.Thread):
    def __init__(self, arr, ct2,id):
        threading.Thread.__init__(self)
        self.arr = arr
        self.ct2 = ct2
        self.id = id
    def run(self):
        print "Starting " + self.name
        threadTest(self.arr, self.ct2,self.id)
        print "Exiting " + self.name

def div_list(ls,n):
    if not isinstance(ls,list) or not isinstance(n,int):
        return []
    ls_len = len(ls)
    if n<=0 or 0==ls_len:
        return []
    if n > ls_len:
        return []
    elif n == ls_len:
        return [[i] for i in ls]
    else:
        j = ls_len/n
        k = ls_len%n
        ls_return = []
        for i in xrange(0,(n-1)*j,j):
            ls_return.append(ls[i:i+j])
        ls_return.append(ls[(n-1)*j:])
        return ls_return

def threadTest(arr,ct2,id):
    fobj = open(PTH+ct2+'.csv','a')
    fobj.truncate()
    rege = ur"([0-9]{1,3}\.){3}[0-9]{1,3}"
    for ip in arr:
        if re.match(rege, ip):
            try:
                fp = urllib2.urlopen("http://"+ip,timeout=2)
                fobj.write(ip+",")
                print " %d->%s" % (id,ip)
            except Exception, e:
                continue
    fobj.close()

count = 0
while(count<FLC):
    ct1 = str(count)
    file_object = open(PTH+ct1+'.csv')
    count += 1
    ct2 = str(count);
    try:
         all_the_text = file_object.read()
    finally:
         file_object.close( )
    arr = all_the_text.split(',')
    threadList = div_list(arr,THN)
    if len(threadList)==0:
        break
    threadLock = threading.Lock()
    threads = []
    thread = range(THN)
    for i in range(0,THN-1):
        thread[i] = myThread(threadList[i],ct2,i)
    for i in range(0,THN-1):
        thread[i].start()
    for i in range(0,THN-1):
        threads.append(thread[i])

    for t in threads:
        t.join()
    print "Exiting Main Thread"
