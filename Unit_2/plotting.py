import numpy as np
import matplotlib.mlab as mlab
import collections
import matplotlib.pyplot as plt
import scipy.stats as stats

#plotting frequencies
# testlist = [1, 4, 5, 6, 9, 9, 9]
#
# # show frequency of each number in list
# c = collections.Counter(testlist)
# count_sum = sum(c.values())
# print(count_sum)
#
# # plotting standard deviation
# mean = 0
# variance = 1
# sigma = np.sqrt(variance) # standard deviation
# x = np.linspace(-3, 3, 100)
# plt.plot(x, mlab.normpdf(x, mean, sigma))
# plt.show()
#
# # box plot
# x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
# plt.boxplot(x)
# plt.show()
#
# # histogram
# plt.hist(x, histtype="bar")
# plt.show()
#
# #qq plot
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show()
plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show()
