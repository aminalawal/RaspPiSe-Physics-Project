
# imports the necessary modules for this program
from sense_hat import SenseHat
import random
import time
import csv

# creates an instance of the sensehat
sense = SenseHat()
# initialize variables
csvfile="acc_user1.csv"
timeXY=0
time_interval=0.05

# defininig colors to be used by the LEDs
red = [255, 0, 0] 
green=[0,255,0]
white=[255,255,255]
blue = [0, 0, 255]
aqua = [0,255,255]
blk=[0,0,0]

## function to store acceleration values in a CSV file
def storeXY_values():
    
    data = [timeXY,accx,timeXY,accy]
    with open(csvfile, "a") as output:
            writer = csv.writer(output,delimiter=",", lineterminator ='\n')
            writer.writerow(data)

# function to  obtain X,Y,Z acceleration values
def get_acc():

    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x=round(x, 2)
    y=round(y, 2)
    z=round(z, 2)
    return x,y,z

# gets the acceleration values at rest
a,b,c = get_acc()
print("acc at rest is",a,b,c)
sense.set_pixel(3,4,red)

## This is the LED light monitoring of the accelerometer begins
while True:
    
    x,y,z = get_acc()
    print ("x,y,z is", x,y,z)
    
# subtracts the value at rest from the subsequent values
    accx=round((x-a),2)
    accy=round((y-b),2)
    accz=round((z-c),2)

    print ("subtracted values are", accx,accy,accz)
    
# positive values
    if(accx<=0.25)&(accx>0):
        sense.set_pixel(7,4,blk)
        sense.set_pixel(6,4,blk)
        sense.set_pixel(2,4,blk)
        sense.set_pixel(1,4,blk)
        sense.set_pixel(0,4,blk)
        sense.set_pixel(5,4,blk)
        sense.set_pixel(4,4,aqua)

    if(accy<=0.25)&(accy>0):
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,1,blk)
        sense.set_pixel(3,2,blk)
        sense.set_pixel(3,5,blk)
        sense.set_pixel(3,6,blk)
        sense.set_pixel(3,7,blk) 
        sense.set_pixel(3,3,white)              

    if(accx<=0.5)&(accx>0.25):
        sense.set_pixel(7,4,blk)
        sense.set_pixel(2,4,blk)
        sense.set_pixel(1,4,blk)
        sense.set_pixel(0,4,blk)
        sense.set_pixel(6,4,blk)
        sense.set_pixel(4,4,aqua)
        sense.set_pixel(5,4,aqua)

    if(accy<=0.5)&(accy>0.25):
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,1,blk)
        sense.set_pixel(3,5,blk)
        sense.set_pixel(3,6,blk)
        sense.set_pixel(3,7,blk) 
        sense.set_pixel(3,3,white)
        sense.set_pixel(3,2,white)      

    if(accx<=0.75)&(accx>0.5):
        sense.set_pixel(2,4,blk)
        sense.set_pixel(1,4,blk)
        sense.set_pixel(0,4,blk)
        sense.set_pixel(7,4,blk)
        sense.set_pixel(4,4,aqua)
        sense.set_pixel(5,4,aqua)
        sense.set_pixel(6,4,aqua)

    if(accy<=0.75)&(accy>0.5):
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,5,blk)
        sense.set_pixel(3,6,blk)
        sense.set_pixel(3,7,blk) 
        sense.set_pixel(3,3,white)
        sense.set_pixel(3,2,white)
        sense.set_pixel(3,1,white)        

    if(accx<=1.0)&(accx>0.75):
        sense.set_pixel(2,4,blk)
        sense.set_pixel(1,4,blk)
        sense.set_pixel(0,4,blk)
        sense.set_pixel(4,4,aqua)
        sense.set_pixel(5,4,aqua)
        sense.set_pixel(6,4,aqua)
        sense.set_pixel(7,4,aqua)

    if(accy<=1.0)&(accy>0.75):
        sense.set_pixel(3,5,blk)
        sense.set_pixel(3,6,blk)
        sense.set_pixel(3,7,blk) 
        sense.set_pixel(3,3,white)
        sense.set_pixel(3,2,white)
        sense.set_pixel(3,1,white)
        sense.set_pixel(3,0,white)

    if(accx>1.0):
        sense.set_pixel(2,4,blk)
        sense.set_pixel(1,4,blk)
        sense.set_pixel(0,4,blk)
        sense.set_pixel(4,4,red)
        sense.set_pixel(5,4,red)
        sense.set_pixel(6,4,red)
        sense.set_pixel(7,4,red)

    if(accy>1.0):
        sense.set_pixel(3,5,blk)
        sense.set_pixel(3,6,blk)
        sense.set_pixel(3,7,blk) 
        sense.set_pixel(3,3,red)
        sense.set_pixel(3,2,red)
        sense.set_pixel(3,1,red)
        sense.set_pixel(3,0,red)
        
 ## Negative Values        

    if(accx>=-0.33)&(accx<0):
        sense.set_pixel(0,4,blk)
        sense.set_pixel(1,4,blk)
        sense.set_pixel(4,4,blk)
        sense.set_pixel(5,4,blk)
        sense.set_pixel(6,4,blk)
        sense.set_pixel(7,4,blk)
        sense.set_pixel(2,4,aqua)

    if(accy>=-0.33)&(accy<0):
        sense.set_pixel(3,6,blk)
        sense.set_pixel(3,7,blk) 
        sense.set_pixel(3,3,blk)
        sense.set_pixel(3,2,blk)
        sense.set_pixel(3,1,blk)
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,5,white)        

    if(accx>=-0.66)&(accx<-0.33):
        sense.set_pixel(0,4,blk)
        sense.set_pixel(4,4,blk)
        sense.set_pixel(5,4,blk)
        sense.set_pixel(6,4,blk)
        sense.set_pixel(7,4,blk)
        sense.set_pixel(2,4,aqua)
        sense.set_pixel(1,4,aqua)

    if(accy>=-0.66)&(accy<-0.33):
        sense.set_pixel(3,7,blk) 
        sense.set_pixel(3,3,blk)
        sense.set_pixel(3,2,blk)
        sense.set_pixel(3,1,blk)
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,5,white)
        sense.set_pixel(3,6,white)       
        
    if(accx>=-1.0)&(accx<-0.66):
        sense.set_pixel(4,4,blk)
        sense.set_pixel(5,4,blk)
        sense.set_pixel(6,4,blk)
        sense.set_pixel(7,4,blk)
        sense.set_pixel(2,4,aqua)
        sense.set_pixel(1,4,aqua)
        sense.set_pixel(0,4,aqua)

    if(accy>=-1.0)&(accy<-0.66): 
        sense.set_pixel(3,3,blk)
        sense.set_pixel(3,2,blk)
        sense.set_pixel(3,1,blk)
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,5,white)
        sense.set_pixel(3,6,white)
        sense.set_pixel(3,7,white)
        
    if(accx<-1.0):
        sense.set_pixel(4,4,blk)
        sense.set_pixel(5,4,blk)
        sense.set_pixel(6,4,blk)
        sense.set_pixel(7,4,blk)
        sense.set_pixel(2,4,red)
        sense.set_pixel(1,4,red)
        sense.set_pixel(0,4,red)

    if(accy<-1.0):
        sense.set_pixel(3,3,blk)
        sense.set_pixel(3,2,blk)
        sense.set_pixel(3,1,blk)
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,5,red)
        sense.set_pixel(3,6,red)
        sense.set_pixel(3,7,red)
        
    if(accx==0.00):
        sense.set_pixel(4,4,blk)
        sense.set_pixel(5,4,blk)
        sense.set_pixel(6,4,blk)
        sense.set_pixel(7,4,blk)
        sense.set_pixel(2,4,blk)
        sense.set_pixel(1,4,blk)
        sense.set_pixel(0,4,blk)
        sense.set_pixel(3,4,red)

    if(accy==0.00):
        sense.set_pixel(3,3,blk)
        sense.set_pixel(3,2,blk)
        sense.set_pixel(3,1,blk)
        sense.set_pixel(3,0,blk)
        sense.set_pixel(3,5,blk)
        sense.set_pixel(3,6,blk)
        sense.set_pixel(3,7,blk)
        sense.set_pixel(3,4,red)
        
# increments time value according to the time interval        
    timeXY+=time_interval
    timeXY=round(timeXY,2)
    
    print(timeXY)
    
#   calling the store values function 
    storeXY_values()
    
    time.sleep(time_interval)

