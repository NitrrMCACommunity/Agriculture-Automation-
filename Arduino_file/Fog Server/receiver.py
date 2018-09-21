from xbee import ZigBee
import serial
import requests
import array
import struct
import XBee
from XBee import XBeeAddress64

 
PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
 
def hex(bindata):
    return ''.join('%02x' % ord(byte) for byte in bindata)
 
ser = serial.Serial(PORT, BAUD_RATE)
 
xbee = ZigBee(ser,escaped=True)

 
while True:
    data=array('I',[0,0,0,0,0,0,0,0])
    XBeeAddress64 add(13A200,41665852)
    add.setMsb(0)
    add.setLsb(0)
    ZBTxRequest zbTx = ZBTxRequest(add, data, sizeof(data))
    xbee.send(zbTx)
    delay(5000)
    try:
        response = xbee.wait_read_frame()
        sa = hex(response['source_addr_long'][4:])
        rf = hex(response['rf_data'])
        
        datalength=len(rf)
        if datalength==32:
            h=int(struct.unpack('f',response['rf_data'][0:4])[0])
            t=int(struct.unpack('f',response['rf_data'][4:8])[0])
            s=int(struct.unpack('f',response['rf_data'][8:12])[0])
            id=int(struct.unpack('f',response['rf_data'][12:16])[0])
            r=requests.post("http://iotproject.us-east-2.elasticbeanstalk.com/sendToCloud?id=154&S="+str(s)+"&H="+str(h)+"&T="+str(t)+"&W=200")
            print s
            print(r.status_code)
        else:
            print (sa,rf)
    except KeyboardInterrupt:
        break
         
ser.close()
