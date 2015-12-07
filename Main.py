'''
Created on Dec 3, 2015

@author: Ben Bertrands
'''
from ipaddress import ip_address
import socketserver
from ServoControl import ServoControl
from MPUControl import MPUControl
from socketserver import BaseRequestHandler


class MyUDPHandler(socketserver.BaseRequestHandler):
    
    print("class: MyUDPHandler")
    servocontroller=ServoControl()
    mpucontroller=MPUControl()
    
    def sendMPUData(self,socket):
        print("sendMPUData")
        socket = self.request[1]
        #self.request.sendall("gyro:".encode(encoding='utf_8'))
        sendsel=""
        for data in MyUDPHandler.mpucontroller.getGyro():
            
            sendsel=sendsel+((str(data)+":"))
        
        #self.request.sendall("am:".encode(encoding='utf_8'))
        for data in MyUDPHandler.mpucontroller.getAM():
            
            sendsel=sendsel+((str(data)+":"))         
            
        socket.sendto(sendsel.encode(encoding='utf_8', errors='strict'),self.client_address)
        
    def handleInput(self,input,socket):
        print("handleInput:"+input.decode(encoding='utf_8', errors='strict'))
        self.sendMPUData(socket)
        try:
            m=input.decode(encoding='utf_8', errors='strict')
            m=m.split(sep=":")
            
            servo=round(float(m[0]))
            #print("servo: "+str(servo))
            pw=round(float(m[1]))
            #print("pw: "+str(pw))
            MyUDPHandler.servocontroller.setServoTo(servo,pw)
            
        except TypeError:
            
            #print("TypeError")
            self.sendMPUData(socket)
        except ValueError:
            self.sendMPUData(socket)
        
    def handle(self):
        print("handle")
        #check if servocontrollers are calibrated, if not calibrate
        if not (MyUDPHandler.servocontroller.init):
            MyUDPHandler.servocontroller.initESC()
            MyUDPHandler.servocontroller.init=True
        data = self.request[0].strip()
        socket = self.request[1]   
        self.handleInput(data,socket)
   
       
       
   
        
if __name__ == "__main__":
    HOST, PORT = "192.168.4.1", 9999
    #self.servocontroller.initESC()
    # Create the server, binding to localhost on port 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.allow_reuse_address=True
    server.timeout=5
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    
    server.serve_forever()
    
  

    
