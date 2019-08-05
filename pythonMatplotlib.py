from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
from pylab import randn

print ("------")
print ("Draw:")
#CHOOSE DRAW (GRAPH:0; PIE CHART:1; BAR CHART:2; SCATTER PLOT:3; HISTOGRAM:4)
v = 4

if (v==0):
    
   #DRAWING A LINE GRAPH 
   #CREATING NUMBERS IN A GIVEN INTERVAL (INITIAL, FINAL, INCREMENT)
   x = np.arange(-3, 3, 0.01)

   #MULTIPLE PLOTS ON ONE GRAPH
   #NORMAL/GAUSSIAN DISTRIBUTION
   plt.plot(x, norm.pdf(x), 'b-') #CHANGING LINE TYPES AND COLORS (:, -., --, -, ...; b, g, r, ....)
   #plt.plot(x, norm.pdf(x))

   #NORMAL/GAUSSIAN DISTRIBUTION (x, mean, std)
   plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:') #CHANGING LINE TYPES AND COLORS
   #plt.plot(x, norm.pdf(x, 1.0, 0.5))

   #ADJUSTING THE AXES
   axes = plt.axes() #CREATING AXES
   axes.set_xlim([-5, 5]) #SETTING X LIMITS
   axes.set_ylim([0, 1.0]) #SETTING Y LIMITS
   axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) #SETTING X
   axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]) #SETTING Y

   #ADDING GRID
   axes.grid()

   #LABELING AXES 
   plt.xlabel('Greebles')
   plt.ylabel('Probability')

   #ADDING LEGEND (loc changes the legend position)
   plt.legend(['Sneetches', 'Gacks'], loc=2)

   #SAVING IT TO A FILE
   plt.savefig('/home/markjr/data_science/DataScience/DataScience-Python3/pythonMatplotlib.png', format='png')

if (v==1):

   #DRAWING A PIE CHART 
   #CREATING NUMBERS 
   values = [12, 55, 4, 32, 14]

   #SETTING COLORS
   colors = ['r', 'g', 'b', 'c', 'm']

   #EXPLODE (array which specifies the fraction of the radius with which to offset each wedge)
   explode = [0, 0, 0.2, 0, 0]

   #SETTING LABELS
   labels = ['India', 'United States', 'Russia', 'China', 'Europe']
     
   #SETTING TITLE
   plt.title('Student Locations')

   #CREATING PIE CHART
   plt.pie(values, colors= colors, labels=labels, explode = explode)

if (v==2):
   #DRAWING A BAR CHART
   #CREATING NUMBERS 
   values = [12, 55, 4, 32, 14]

   #SETTING COLORS
   colors = ['r', 'g', 'b', 'c', 'm']
   
   #CREATING A BAR CHART
   plt.bar(range(0,5), values, color= colors) 
      
if (v==3):
   #DRAWING A BAR CHART
   #CREATING NUMBERS 
   X = randn(500)
   Y = randn(500)
   
   #CREATING A BAR CHART
   plt.scatter(X,Y)
   
if (v==4):
   #DRAWING A HISTOGRAM
   #CREATING NUMBERS 
   incomes = np.random.normal(27000, 15000, 10000)
   
   #CREATING HISTOGRAM
   plt.hist(incomes, 50)

plt.show()
