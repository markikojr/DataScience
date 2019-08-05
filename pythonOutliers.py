import numpy as np
import matplotlib.pyplot as plt

#GENERATING RANDOM VALUES
incomes = np.random.normal(27000, 15000, 10000)

#GENERATING OUTLIER
incomes = np.append(incomes, [1000000000])

#GETTING THE MEAN
print ('Mean with outlier:',incomes.mean())

#REMOVING OUTLIERS (it filters out anything beyond two standard deviations of the median value in the data set)
def reject_outliers(data):
    u = np.median(data)
    s = np.std(data)
    filtered = [e for e in data if (u - 2 * s < e < u + 2 * s)]
    return filtered

filtered = reject_outliers(incomes)

#plt.hist(filtered, 50)

plt.subplot(2, 1, 1)
plt.hist(incomes, 50)
plt.title('Outlier removal')
plt.ylabel('# of entries')

plt.subplot(2, 1, 2)
plt.hist(filtered, 50)
plt.xlabel('$')
plt.ylabel('# of entries')
plt.show()

print ('Mean without outlier:',np.mean(filtered))