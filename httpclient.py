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
    r = requests.get("http://localhost:8080/getVMS")
    vmInfo = json.loads(r.text)

    vm1Name = vmInfo["VM1"]["name"]
    vm2Name = vmInfo["VM2"]["name"]
    vm1IP = vmInfo["VM1"]["ip"]
    vm2IP = vmInfo["VM2"]["ip"]

    vmNameAndTime = [];
    i = 0;
    while  i < 10:
        start = default_timer()

        #Get load....
        r2 = requests.get("http://localhost:8080/getLoad/" + vm1Name)
        r3 = requests.get("http://localhost:8080/getLoad/" + vm2Name)
        vmLoads1 = json.loads(r2.text);
        vmLoads2 = json.loads(r3.text);

        load1 = vmLoads1["load"]
        load2 = vmLoads2["load"]
        currentMachine = ""

        print "Load1: " + str(load1)
        print "Load2: " + str(load2)

        #Post
        if load1 < load2:
            r4 = requests.post("http://localhost:8080/n", data = {"number":i,"vm":vm1Name})
            print("Is " + str(i) + " a prime?")
            print(r4.text)
            currentMachine = vm1Name;
        else:
            r5 = requests.post("http://localhost:8080/n", data = {"number":i,"vm":vm2Name})
            print("Is " + str(i) + " a prime?")
            print(r5.text)
            currentMachine = vm2Name

        duration = default_timer() - start
        vmNameAndTime.append((currentMachine,duration))
        print(currentMachine,duration)
        i += 1

    #for vmAndDuration in vmNameAndTime:
    #   print(vmAndDuration)
# invoke main
if __name__ == "__main__":
    sys.exit (main ())
