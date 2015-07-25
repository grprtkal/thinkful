import collections as c
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

numlist = [1, 4, 5, 6, 9, 9, 9]

# frequency
freq = c.Counter(numlist)
print(freq)

# boxplot
plt.boxplot(numlist)
plt.title("Boxplot of Numbers")
plt.savefig("boxplot.png")

# histogram
plt.hist(numlist, histtype="bar")
plt.title("Histogram of Numbers")
plt.savefig("histogram.png")

# qq-plot
plt.figure()
norm_numlist = np.random.normal(numlist)
stats.probplot(norm_numlist, dist="norm", plot=plt)
plt.savefig("qqplot.png")

