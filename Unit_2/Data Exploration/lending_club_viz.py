import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv("loansData.csv")

# remove rows with null values
loansData.dropna(inplace=True)

# data exploration
# box plot of loan amounts funded by investors
loansData.boxplot(column="Amount.Funded.By.Investors")
plt.show()

# histogram of loan amounts funded by investors
loansData.hist(column="Amount.Funded.By.Investors")
plt.show()

# qq-plot
plt.figure()
graph = stats.probplot(loansData["Amount.Funded.By.Investors"], dist="norm", plot=plt)
plt.show()

