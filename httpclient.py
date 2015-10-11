#!/bin/python
#  TEST
# sample http client
# TEST
import sys
import httplib
import requests
import json
import demjson

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

r = requests.get("http://localhost:8888/getVMS")
vmInfo = json.loads(r.text)
vm1 = vmInfo["VM1"]
vm2 = vmInfo["VM2"]

print(vm1)
print(vm2)

#Get load....
r2 = requests.get("http://localhost:8888/getLoad")
vmLoads = json.loads(r2.text);
load1 = vmLoads["VM1"]["load"]
load2 = vmLoads["VM2"]["load"]

number = raw_input("Please enter a number: ")

dataToPost1 = [ { vm1["name"]: number } ]
send1 = demjson.encode(dataToPost1)

dataToPost2 = [ { vm2["name"]: number } ]
send2 = demjson.encode(dataToPost2)

#Post
if load1 < load2:
    r3 = requests.post("http://localhost:8888/checkForPrimes", send1)
    print("Is " + number + " a prime?")
    print(r3.text)
else:
    r4 = requests.post("http://localhost:8888/checkForPrimes", send2)
    print("Is " + number + " a prime?")
    print(r4.text)


# invoke main
if __name__ == "__main__":
    sys.exit (main ())