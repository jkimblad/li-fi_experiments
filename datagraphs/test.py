#!/usr/bin/env python3

# library and dataset
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import random
 
def main():
    speedGraph()


def speedGraph():
    dataFrame = pd.DataFrame({
        'x' : [0, 1, 10, 100, 1000, 10000, 100000, 250000, 500000, 750000, 1000000], 
        'y' : speedData(),
        })
     
    # plot with matplotlib
    plt.title("Transfer-speeds effect on error-rates")
    plt.xlabel("Transfer-speed (Hz)")
    plt.ylabel("Error-rate (%)")
    plt.semilogx( 'x', 'y', data=dataFrame, marker='o', color='mediumvioletred')
    plt.show()

def speedData():
    return [0, 0, 0, 0, 0, 0, 25, 50, 75, 100, 100]

def distanceGraph():
    dataFrame = pd.DataFrame({
        'x' : np.linspace(10, 100, 9),
        'y' : distance(),
        })
     
    # plot with matplotlib
    plt.title("Error-rate as function of distance")
    plt.xlabel("Distance (cm)")
    plt.ylabel("Error-rate (%)")
    plt.plot( 'x', 'y', data=dataFrame, marker='o', color='mediumvioletred')
    plt.show()

def distance():
    dataList = list()
    for i in range(1, 7):
        dataList.append((i**4)/32 * random.uniform(0.8, 1.2))
    dataList.extend([100, 100, 100])
    
    return dataList


def pathLossGraph():
    dataFrame = pd.DataFrame({
        'x' : range(1, 10),
        'y' : pathLoss(),
        })
     
    # plot with matplotlib
    plt.title("Free-space path loss")
    plt.xlabel("Distance")
    plt.ylabel("Signal strength")
    plt.loglog( 'x', 'y', data=dataFrame, marker='o', color='mediumvioletred')
    plt.show()


def pathLoss():
    lossList = list()
    for i in np.linspace(0.01, 0.1, 9):
        lossList.append(1/((4*math.pi*i)**(2)) * random.uniform(0.9, 1.1))

    return lossList

if __name__ == "__main__":
    main()
