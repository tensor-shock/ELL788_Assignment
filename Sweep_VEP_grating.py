import matplotlib
import matplotlib.pyplot as plt
import time
import math

frequency=10        #to be kept 10
time_per_cpd=10     #to be kept 30

for cpm in range(1,21,2):

    print("Showing the Sweep VEP grating for {} cycles per degree".format(cpm))
    thickness=100
    cycle_width=2*thickness
    number_of_cycles=math.ceil(1000/cycle_width)

    x_pts=[]
    for j in range(number_of_cycles):
        x_pts.append(j*cycle_width)

    number_of_cycles=math.floor((time_per_cpd*frequency)/2)
    pause_time=1/frequency

    for cycle in range(number_of_cycles):
        #on phase
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for x in x_pts:
            rect=matplotlib.patches.Rectangle((x, 0),thickness, 1000, color ='black')
            ax.add_patch(rect)
        plt.xlim([0, 1000])
        plt.ylim([0, 1000])

        plt.pause(pause_time)

        #off phase
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for x in x_pts:
            rect=matplotlib.patches.Rectangle((x+thickness, 0),thickness, 1000, color ='black')
            ax.add_patch(rect)
        plt.xlim([0, 1000])
        plt.ylim([0, 1000])

        plt.pause(pause_time)

