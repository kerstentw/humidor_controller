import serial 
import requests
import os

"""
This is the conversion table to go from the site Json to the 
Halmidifier Assembly.

conversion = {
"A" : "hi_limit",
"B" : "low_limit",
"C" : "on_once ",
"D" : "on_override" , 
"E" : "off_once",
"F" : "off_override",
"G" : "calibrate",
}

Setting things like limits will be structured and sent down the serial
as such:

'A 4.55'  -> This will set the hi_limit to 4.55.  On the humidifier end
the number will be converted to a float so dont worry about sending
integers vs. floats

"""

SITE_ENDPOINT = "http://budongsanbud-halmidor.rhcloud.com/comm?"

conversion = {
"A" : "hi_limit",
"B" : "low_limit",
"C" : "on_once ",
"D" : "on_override" , 
"E" : "off_once",
"F" : "off_override",
"G" : "calibrate",
}



def determine_serial_port():
    
    root = '/dev/serial/by-path'
    try:
        name_of_port = os.listdir(root)[0]
        full_path = root + name_of_port
        print "connecting with: {}".format(full_path)
        return full_path   
    except:
        print "No Serial connection detected"


def send_info_to_endpoint(to_send):
    send_frame = "%s" % to_send
    resp = requests.get(SITE_ENDPOINT + "%s")
    return resp.content()

ser_conn = serial.Serial('/dev/serial/by-path/platform-3f980000.usb-usb-0:1.2:1.0-port0',9600)

while True:
    print ser_conn.readline()
    ser_conn.write("A 54.4")
