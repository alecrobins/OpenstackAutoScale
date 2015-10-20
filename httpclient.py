#!/bin/python
#  TEST
# sample http client
# TEST
import sys
import httplib
import requests
import json
from timeit import default_timer

def main ():
    print "Instantiating a connection obj"
    try:
        conn = httplib.HTTPConnection ("localhost", "8888")
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise
    
    print "sending a GET request to our http server"
    try:
        conn.request ("GET", "/")
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise
    
    print "retrieving a response from http server"
    try:
        resp = conn.getresponse ()
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise
    
    print "printing response headers"
    try:
        for hdr in resp.getheaders ():
            print hdr
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise
    
    print "printing data"
    try:
        data = resp.read ()
        print "Length of data = ", len(data)
        print data
    except:
        print "Exception thrown: ", sys.exc_info()[0]
        raise

r = requests.get("http://localhost:8080/getVMS")
vmInfo = json.loads(r.text)

vm1Name = vmInfo["VM1"]["name"]
vm2Name = vmInfo["VM2"]["name"]
vm1IP = vmInfo["VM1"]["ip"]
vm2IP = vmInfo["VM2"]["ip"]

i = 0;
durationsOfCalls = []
if  i < 1000:
    start = default_timer()

    #Get load....
    r2 = requests.get("http://localhost:8080/getLoad", vm1Name)
    r3 = requests.get("http://localhost:8080/getLoad", vm2Name)
    vmLoads1 = json.loads(r2.text);
    vmLoads2 = json.loads(r3.text);

    load1 = vmLoads1["load"]
    load2 = vmLoads2["load"]

    #Post
    if load1 < load2:
        r4 = requests.post("http://localhost:8080/checkForPrimes", data = {"number":i,"vm":vm1Name})
        print("Is " + i + " a prime?")
        print(r4.text)
    else:
        r5 = requests.post("http://localhost:8080/checkForPrimes", data = {"number":i,"vm":vm2Name})
        print("Is " + i + " a prime?")
        print(r5.text)

    duration = default_timer() - start
    durationsOfCalls.append(duration)
    ++i

print durationsOfCalls

# invoke main
if __name__ == "__main__":
    sys.exit (main ())
