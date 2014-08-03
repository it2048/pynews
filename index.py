__author__ = 'it2048'

import urllib2
import socket
import re
import time
#set default timeout
socket.setdefaulttimeout(1)


count = 0
#Iteration 5 times,you can modify
while(count<5):
    ct1 = str(count)
    #ip0.txt file use to store google ip
    file_object = open('ip'+ct1+'.txt')
    count = count+1
    ct2 = str(count);
    fobj = open('ip'+ct2+'.txt','a')
    fobj.truncate()
    try:
         all_the_text = file_object.read()
    finally:
         file_object.close( )
    arr = all_the_text.split(',')
    rege = ur"([0-9]{1,3}\.){3}[0-9]{1,3}"
    for ip in arr:
        if re.match(rege, ip):
            try:
                start = time.clock()
                fp = urllib2.urlopen("http://"+ip,timeout=1)
                end = time.clock()
                fobj.write(ip+",")
                print "%s %f" %(ip,end-start)
            except Exception, e:
                continue
    fobj.close()









