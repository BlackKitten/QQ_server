'''
Created on Dec 3, 2015

@author: Ben Bertrands
'''
import smbus
import time
import math

bus = smbus.SMBus(1)
base_address = 0x68 #i2cdetect
power1=0x6b
power2=0x6c
gyrox=0x43
gyroy=0x45
gyroz=0x47
amx=0x3b
amy=0x3d
amz=0x3f


class MPUControl(object):
    '''
    classdocs
    '''


    def __init__(self):
        #disable powersave
        bus.write_byte_data(base_address,power1,0)
        
    def get_byte(self,adr):
        bus.read_byte()
   
    
    def read_byte(self,adr):

        return bus.read_byte_data(base_address, adr)
 

    def read_word(self,adr):
    
        high = bus.read_byte_data(base_address, adr)
    
        low = bus.read_byte_data(base_address, adr+1)
    
        val = (high << 8) + low
    
        return val
    
     
    
    def read_word_2c(self,adr):
    
        val = self.read_word(adr)
    
        if (val >= 0x8000):
    
            return -((65535 - val) + 1)
    
        else:
    
            return val
    
     
    
    def dist(self,a,b):
    
        return math.sqrt((a*a)+(b*b))
    
     
    
    def get_y_rotation(self,x,y,z):
    
        radians = math.atan2(x, self.dist(y,z))
    
        return -math.degrees(radians)
    
     
    
    def get_x_rotation(self,x,y,z):
    
        radians = math.atan2(y, self.dist(x,z))
    
        return math.degrees(radians)

    def getGyro(self):
        return [self.read_word_2c(gyrox),self.read_word_2c(gyroy),self.read_word_2c(gyroz)]
    
    def getAM(self):
        return [self.read_word_2c(amx),self.read_word_2c(amy),self.read_word_2c(amz)]
        