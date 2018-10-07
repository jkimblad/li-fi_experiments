#!/usr/bin/env python3

# Dataset
import data

# Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random

def main():
    LEDDistanceGraph()

def LEDDistanceGraph():
    # Import data for red LED
    redDataFrame = pd.DataFrame({
        'x' : data.redLEDDistanceDataX,
        'y' : data.redLEDDistanceDataY,
        })
    # Import data for blue LED
    blueDataFrame = pd.DataFrame({
        'x' : data.blueLEDDistanceDataX,
        'y' : data.blueLEDDistanceDataY,
        })
    # Import data for yellow LED
    yellowDataFrame = pd.DataFrame({
        'x' : data.yellowLEDDistanceDataX,
        'y' : data.yellowLEDDistanceDataY,
        })
    # Import data for green LED
    greenDataFrame = pd.DataFrame({
        'x' : data.greenLEDDistanceDataX,
        'y' : data.greenLEDDistanceDataY,
        })

    # Define each line
    # IMPORTANT! Use "tableau 20" color palette when choosing colors for graphics in report
    plt.plot('x', 'y', data = redDataFrame, marker = 'o', color = 'red')
    plt.plot('x', 'y', data = blueDataFrame, marker = 'o', color = 'blue')
    plt.plot('x', 'y', data = yellowDataFrame, marker = 'o', color = 'yellow')
    plt.plot('x', 'y', data = greenDataFrame, marker = 'o', color = 'green')
    # Plot settings
    # plt.title("Error-rates as function of distance for red LED")
    plt.xlabel("Distance (mm)")
    plt.ylabel("Erroneous readings (bits)")
    plt.show()



if __name__ == "__main__":
    main()

