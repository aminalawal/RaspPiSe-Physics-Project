# imports the necessarry modules needed to run this script
import time
import csv
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED

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

# creates an instance of the sensehat
sense = SenseHat()

# initializes a name for the csv file in which values willbe stored
csvfile = "gaylussac.csv"

# function that makes the joystick clear the LED screen when pushed down
def pushed_down(event):
    sense.clear()

    
while True:
    
    temp = sense.get_temperature()
    temp = round(temp, 2)
    
        
    prezzure =sense.get_pressure()
    prezzure = round(prezzure, 2)  

    
    print ("Temperature is ", temp)
    print ("Pressure is ",prezzure)
    
    data = [temp,prezzure]
    
   
# command to store the data in a csv file
    with open(csvfile, "a") as output:
            writer = csv.writer(output,delimiter=",", lineterminator ='\n')
            writer.writerow(data)
    
            
# command to call the joystick function
    sense.stick.direction_down = pushed_down
    
# timer that makes the loop run every 30 seconds.
    time.sleep(30)
    

