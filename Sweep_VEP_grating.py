import matplotlib
import matplotlib.pyplot as plt
import time
import math

frequency=10        #to be kept 10
time_per_cpd=30     #to be kept 30

#one cycle in ~2 cm screen space kept at 114 cm has 1 cpd
#1 unit of thickness in python = 0.02 cm
#one cycle in 100 units screen space kept at 114 cm has 1 cpd
#one cycle in 100/x units screen space kept at 114 cm has x cpd

#OBSERVER'S EYE IS TO BE KEPT AT 114 CMS FROM THE SCREEN

for cpd in range(1,21,2):  #(1,21,2)

    print("Showing the Sweep VEP grating for {} cycles per degree".format(cpd))
    cycle_width=100/cpd
    thickness=cycle_width/2
    #cycle_width=2*thickness
    number_of_cycles=math.ceil(1000/cycle_width)

    x_pts=[]
    for j in range(number_of_cycles):
        x_pts.append(j*cycle_width)

    number_of_cycles=math.floor((time_per_cpd*frequency)/2)
    pause_time=1/frequency

    for cycle in range(number_of_cycles):
        
        #first phase
        fig = plt.figure(figsize=(12, 7))
        plt.title('{} cpd'.format(cpd))
        ax = fig.add_subplot(111)
        for x in x_pts:
            rect=matplotlib.patches.Rectangle((x, 0),thickness, 1000, color ='black')
            ax.add_patch(rect)
        plt.xlim([0, 1000])
        plt.ylim([0, 1000])

        plt.pause(pause_time)
        plt.close()


        
        #second phase
        fig = plt.figure(figsize=(12, 7))
        plt.title('{} cpd'.format(cpd))
        ax = fig.add_subplot(111)
        for x in x_pts:
            rect=matplotlib.patches.Rectangle((x+thickness, 0),thickness, 1000, color ='black')
            ax.add_patch(rect)
        plt.xlim([0, 1000])
        plt.ylim([0, 1000])

        plt.pause(pause_time)
        plt.close()

