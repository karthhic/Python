from cpppo.server.enip import client
import sys
import time
print(" ")
print("Output:")
timeout=10
port=44818
speed = 0
i=0
IP = raw_input("Enter the IP address of the PLC: ")      #"192.168.0.100"

fo = open("tags.txt", "r+")
print "Name of the file: ", fo.name
line = fo.readlines()
print "select a tag to read"
for i in range(0,len(line)):
    line[i]=line[i].replace("\n", "")


def TagData(mode,tag_name, plc_addr):                                                                                                           #Building a function
    with client.connector( host = plc_addr, port = 44818, timeout = timeout ) as conn:                                                          #Creates a UDP connection
        operations              = client.parse_operations( [tag_name] )
        if (mode == "wr"):
            failures,transactions   = conn.process(operations=operations, depth=2, multiple=0,fragment=False, printing=False, timeout=timeout ) #Write Tag
        elif (mode == "rd"):
            for index,descr,op,reply,status,value in conn.pipeline(operations = operations, depth = 2 ):                                        #Read tag
                poz =(value[0])
            if value is None:
                print("None returned while reading %s from PLC %s " % (tag_name, plc_addr))
            return poz
def read(tag):                                               # Function to read a tag value.
    tagout = TagData("rd",tag, IP)
    return tagout
while True:
        for i in range(0,len(line)):
            print str(i+1)+". "+line[i]
        print "0. exit program"
        val  = raw_input("enter the tag number to read: ")
        sel = int(val)
        if sel in range(1,(len(line)+1)):
            op = read(line[sel-1])
            print ((op))
        elif sel == 0:
            print "Code Written in Python by Karthhic"
            time.sleep(3)
            sys.exit()
        else:
            print "Input not acceptable"
