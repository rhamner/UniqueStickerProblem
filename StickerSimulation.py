from random import randint
import matplotlib
import matplotlib.pyplot as plt

#arrays to hold results
hist = [0]*150
cdf = [0]*150

numTrials = 50000   #number of trials to run
numUniques = 7      #number of stickers

#simulate a bunch of trials
for i in range(numTrials):
    vals = [0]*numUniques
    flag = True
    counter = 0

    #iterate until all 5 stickers are found
    while(flag):
        flag = False
        counter += 1

        #try a new sticker
        temp = randint(0, numUniques - 1)
        if(vals[temp] == 0):
            vals[temp] = 1

        #if any are missing, keep going
        for i in range(numUniques):
            if(vals[i] == 0):
                flag = True

    #add result of trial
    hist[counter] += 1

#calculate cdf and average
cdf[0] = hist[0]
sum = 0
for i in range(1, 75):
    cdf[i] = cdf[i - 1] + hist[i]
    sum += hist[i]*(i)

#convert to percentages
for i in range(75):
    cdf[i] = 100*cdf[i]/(numTrials*1.0)
    hist[i] = 100*hist[i]/(numTrials*1.0)

#expectation value
print sum/(numTrials*1.0)

#plot stuff
plt.rcParams['axes.facecolor'] = '#242128'
plt.rcParams['figure.facecolor'] = '#242128'
plt.rcParams['font.size'] = 20
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.figure(1)
plt.plot(range(50), cdf[0:50], color = 'white', linewidth = 3)
plt.xlabel('# of boxes')
plt.ylabel('% of trials that stopped by this # of boxes')
plt.figure(2)
plt.bar(range(50), hist[0:50], color = 'white')
plt.xlabel('# of boxes')
plt.ylabel('% of trials that stop at this # of boxes')
plt.show()




