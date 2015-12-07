'''
Created on Dec 3, 2015

@author: Ben Bertrands
'''
import time
import pigpio

class ServoControl(object):
    init=False
    '''
    classdocs
    '''
    def __init__(self):
        print("__init__")
        self.pi=pigpio.pi()
        
    def stop(self):
        self.pi.stop()
    
    def setServoTo(self,SERVO,pulsewidth):
        pulsewidth=round(pulsewidth)
        print("setServoTo "+str(SERVO)+" "+str(pulsewidth))
        self.pi.set_servo_pulsewidth(SERVO,round(pulsewidth))
        
        
    #pi=pigpio.pi()
    SERVO1 = 4
    SERVO2 = 17
    SERVO3 = 27
    SERVO4 = 22   
     
        
    servos=[ SERVO1, SERVO2, SERVO3, SERVO4 ]
    
    
    def initESC(self):
        print("initESC")
        
        for SERVO in self.servos:
            #pi.set_servo_pulsewidth(SERVO, 1000) # Minimum throttle.
            self.setServoTo(SERVO,1000)
        time.sleep(1)
        for SERVO in self.servos:
            self.setServoTo(SERVO,2000)
            #pi.set_servo_pulsewidth(SERVO, 2000) # Max throttle
        time.sleep(1)
        for SERVO in self.servos:
            #pi.set_servo_pulsewidth(SERVO, 0) #off
            self.setServoTo(SERVO, 0)
    
    
    
        
        