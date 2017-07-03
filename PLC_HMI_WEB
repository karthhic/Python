#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import cgi
from cpppo.server.enip import client
import sys
timeout=1
port=44818
poz = 0
i=0
tag = '0'
IP = '192.168.0.1'
print '<html>'
print '<head><title>X Axis</Title><meta http-equiv="refresh" content="30"></head>'
print '<body>'
form = cgi.FieldStorage()
if form.getvalue("IP"):
	    #global IP
        IP = form.getvalue("IP")
#	print 'Entered IP ' + IP + '</h1><br />'
if form.getvalue("tag 1"):
        #global tag
        tag = "tag 1"
if form.getvalue("tag 2"):
        #global tag
        tag = "tag 2"
def TagData(mode,tag_name, plc_addr):                                                                                                           #Building a function
    with client.connector( host = plc_addr, port = 44818, timeout = timeout ) as conn:                                                          #Creates a UDP connection
        operations              = client.parse_operations( [tag_name] )
        if (mode == "wr"):
            failures,transactions   = conn.process(operations=operations, depth=2, multiple=0,fragment=False, printing=False, timeout=timeout ) #Write Tag
        elif (mode == "rd"):
            for index,descr,op,reply,status,value in conn.pipeline(operations = operations, depth = 2 ):                                        #Read tag
                poz = int(value[0])
            if value is None:
                print("None returned while reading %s from PLC %s " % (tag_name, plc_addr))
            return poz,plc_addr
    time.sleep(.5)
print '<p>Enter your PLC IP addresses</p>'
print '<form method="post" action="PLC_HMI_WEB.py">'
print '<p>IP Address: <input type="text" name="IP"/></p>'
print '<input type="checkbox" name="tag 1" /> tag 1'
print '<input type="checkbox" name="tag 2" /> tag 2'
print '<input type="submit" value="Submit" />'
print '</form>'
print '</body>'
print '</html>'

#print 'EMS1 = TagData("rd",' + tag + ',' +  IP +')' + "\n"

EMS = TagData("rd",tag,IP)

if tag == "tag 1":
	print '\n'+"Value of tag 1"
if tag == "tag 2":
	print '\n'+"Value of tag 2"

print EMS[0]

if tag == "tag 1":
        print "."
if tag == "tag 2":
        print "."
