# imports the necessary modules for this program
from sense_hat import SenseHat
import time
import csv

# creates an instance of the sensehat
sense = SenseHat()

# initialize variables
csvfile="SHM1.csv"
loop_counter=0
time_XY=0
time_interval=0.5

# defininig colors to be used by the LEDs

R = [255, 0, 0]#red
G = [0, 255, 0] #green
B = [0, 0, 255] #blue

# pixel lists in different colors 
red_list = [
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R,
R, R, R, R, R, R, R, R
]

green_list = [
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G,
G, G, G, G, G, G, G, G
]

blue_list = [
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B
]

# function to store acceleration values in a CSV file
def storeXYZ_values():
    
    data = [timeXY,accx,accy,accz]
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

while True:
    
# loop counter keeps track of how many time the loop runs   
    loop_counter+=1
    
# gets the acceleration values in motion
    x,y,z = get_acc()
    print ("x,y,z is", x,y,z)
    
# subtracts the value at rest from the subsequent values
    accx=round((x-a),2)
    accy=round((y-b),2)
    accz=round((z-c),2)

    print ("Acceleration values are", accx,accy,accz)
    
# keeps track of how time increases in each iteration with the time interval value   
    
    time_XY+=time_interval
    print(time_XY)
            
#   call the storeXYZ_values function below 
   
    time.sleep(time_interval)
    
