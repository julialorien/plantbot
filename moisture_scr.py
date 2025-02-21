#this function is to collect sensor readings from the Pimoroni Grow Hat Moisture Sensor
#this function then passes the value back to the main function for the bot to message in chat

from grow.moisture import Moisture
from time import sleep

m1_sensor = Moisture(1)
def grab_moisture():
    #create list of moisture readings to avg
    moistures = []
    for i in range(10):
        capture = m1_sensor.moisture
        moistures.append(capture)
        print(moistures)
        sleep(0.1)
    
    avg_moisture = round(sum(moistures) / len(moistures), 2)
    print(f'Average moisture is {avg_moisture}.')
    return(avg_moisture)