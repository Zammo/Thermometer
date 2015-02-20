import serial
import re
import time
from time import gmtime, strftime

error = True

while error:
    try:
        serial.Serial(2,9600)
        error = False
    except:
        error = True
        print "Error"
    else:
        ser = serial.Serial(2,9600)
        print "Done"

import os
import sys
import math

from pygooglechart import SimpleLineChart
from pygooglechart import Axis



def stripes(data,X_data):
    
    # Set the vertical range from 0 to 100
    max_y = 100

    # Chart size of 200x125 pixels and specifying the range for the Y axis
    chart = SimpleLineChart(600, 400, y_range=[0, max_y])

    chart.add_data(data)
    
    # Set the line colour to blue
    chart.set_colours(['0000FF'])

    # Set the horizontal dotted lines
    chart.set_grid(0, 25, 5, 5)

    # The Y axis labels contains 0 to 100 skipping every 25, but remove the
    # first number because it's obvious and gets in the way of the first X
    # label.
    left_axis = list(range(0, max_y + 1, 5))
    left_axis[0] = ''
    chart.set_axis_labels(Axis.LEFT, left_axis)

    chart.set_axis_labels(Axis.BOTTOM, X_data)

    chart.download('line-stripes.png')

def main():
    data = [0,0,0,0,0,0,0,0,0,0]
    X_data = [0,0,0,0,0,0,0,0,0,0]
    
    while True:
        s = ser.read(9)
        s = s.replace("s","").replace("e","").replace("\r\n","")
        s = float(s)
        
        data.remove(data[0])
        data.append(s)

        X_data.remove(X_data[0]);
        X_data.append(strftime("%H:%M:%S", gmtime()))
                
        stripes(data,X_data)
        time.sleep(1)
        print "OK"

if __name__ == '__main__':
    main()


