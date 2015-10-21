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
<<<<<<< HEAD

=======
>>>>>>> 1b4c9ebdde70de2d1f882756e34e086f2cc44dcb
    r = requests.get("http://localhost:8080/getVMS")
    vmInfo = json.loads(r.text)

    vm1Name = vmInfo["VM1"]["name"]
    vm2Name = vmInfo["VM2"]["name"]
    vm1IP = vmInfo["VM1"]["ip"]
    vm2IP = vmInfo["VM2"]["ip"]

    vmNameAndTime = [];
<<<<<<< HEAD
    while  i < 1000:
=======
    i = 0;
    while  i < 10:
>>>>>>> 1b4c9ebdde70de2d1f882756e34e086f2cc44dcb
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
            currentMachine = vm1Name    
        else:
            currentMachine = vm1Name

        r4 = requests.post("http://localhost:8080/n", data = {"number":i,"vm":currentMachine})
            print("Is " + str(i) + " a prime?")
            print(r4.text)
            currentMachine = vm1Name;

        duration = default_timer() - start
        vmNameAndTime.append((currentMachine,duration))
<<<<<<< HEAD
        durationsOfCalls.append(duration)
        vmCalled.append(currentMachine)
        i += 10
=======
        print(currentMachine,duration)
        i += 1
>>>>>>> 1b4c9ebdde70de2d1f882756e34e086f2cc44dcb

    #for vmAndDuration in vmNameAndTime:
    #   print(vmAndDuration)
# invoke main
if __name__ == "__main__":
    sys.exit (main ())
