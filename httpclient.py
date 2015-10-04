#!/bin/python
#  TEST
# sample http client
# TEST
import sys
import httplib
import requests
import json

r = requests.get('http://localhost:8888/get')
l = requests.get('http://localhost:8888/getLoad')


def getMachineNumber():
    r.json()

def getLoad():
    l.json()

def checkIfPrime():
#TODO: get machine name with lowest load
#send it prime number
prime = {'prime1': '17'}
p = requests.post("http://localhost:8888/checkForPrimes", data=prime)
print(p.text)


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

getMachineNumber()
getLoad()

# invoke main
if __name__ == "__main__":
    sys.exit (main ())
    
