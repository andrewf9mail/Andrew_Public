import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation

# read data
data = pd.read_csv(
    "[your/filepath/here.csv]",
    delimiter=',',
    usecols=[0, 1, 2])

# define days and draw plot
days = ["Mon","Sun","Sat","Fri","Thur","Wed","Tues"]
fig = plt.figure(figsize=(8,8))
ax1 = plt.subplot(111, projection='polar')

# place day labels around plot area (last digit is one more than # of values)
days_angles = np.linspace((np.pi/2)+(2*np.pi),np.pi/2,8)
for i,day in enumerate(days):
    ax1.text(days_angles[i],18.75,day,color="white",fontsize=15,ha="center")

# "bullseye circles"
full_circle_thetas = np.linspace(0, 2*np.pi, 1000)
red_line_zero_radii = [6]*1000
red_line_one_radii = [11]*1000
red_line_two_radii = [16]*1000

# format and label "bullseye"
ax1.plot(full_circle_thetas, red_line_zero_radii, c='white')
ax1.plot(full_circle_thetas, red_line_one_radii, c='white')
ax1.plot(full_circle_thetas, red_line_two_radii, c='white')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.text(np.pi/2, 6, "5 mi", color="white", ha='center', fontdict={'fontsize': 10})
ax1.text(np.pi/2, 11, "10 mi", color="white", ha='center', fontdict={'fontsize': 10})
ax1.text(np.pi/2, 16, "15 mi", color="white", ha='center', fontdict={'fontsize': 10})

# hide degree-marking labels on outside of plot area
ax1.axes.get_xaxis().set_ticklabels([])

# hide ring labels inside plot area
ax1.axes.get_yaxis().set_ticklabels([])

# set size of plot area to accomodate max
ax1.set_ylim(0, 18)

# set graph background to black
ax1.set_facecolor('#000000')

# set window background to gray
fig.set_facecolor("#323331")

theta = np.linspace(0, 2*np.pi, 7)
weeks = data['Week'].unique()

# graph labels
fig.text(.1, 1.10, "#iwouldwalk1000miles, 2021-2022", color="white", fontdict={'fontsize': 20}, transform=ax1.transAxes)
fig.text(-.15, -.1, "Total:", color="white", fontdict={'fontsize': 20}, transform=ax1.transAxes)
fig.text(.40, -.05, "Week", color="white", fontdict={'fontsize': 20}, transform=ax1.transAxes)

# animation
def update(j):
    # Remove the last "week" label to simulate a counter
    for txt in fig.texts:
        if(txt.get_position()==(.55,-0.05)):
            txt.set_visible(False)
    # Specify how we want the plot to change in each frame
    wk = weeks[j]
    r = data[data['Week'] == wk]['Miles'] + 1
    ax1.plot(theta, r, c=plt.cm.viridis(j*5))
    fig.text(.55, -.05, wk, color="white", fontdict={'fontsize': 20}, transform=ax1.transAxes)
    if wk == 52:
        fig.text(0, -.1, "1057.84 miles", color="white", fontdict={'fontsize': 20}, transform=ax1.transAxes)
    return ax1

anim = FuncAnimation(fig, update, frames=len(weeks), interval=200, repeat=False)
anim.save('climate_spiral1.gif', dpi=120, writer='ImageMagickWriter', savefig_kwargs={'facecolor': '#000000'})
plt.show()
