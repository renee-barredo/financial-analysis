# The following code determines whether the average daily return of Microsoft's 
# stock is 0 or not, based on the years of historical data available.

import pandas as pd
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
% matplotlib inline

ms = pd.DataFrame.from_csv('../data/microsoft.csv')
ms['logReturn'] = np.log(ms['Close'].shift(-1)) - np.log(ms['Close'])

ms['logReturn'].plot(figsize=(20, 8))
plt.axhline(0, color='red')
plt.show()

sample_mean = ms['logReturn'].mean()
sample_std = ms['logReturn'].std(ddof=1)
n = ms['logReturn'].shape[0]

# Calculate test statistic 
zhat = (sample_mean - 0)/(sample_std/n**0.5)
print(zhat)

# Set decision criteria
alpha = 0.05
zleft = norm.ppf(alpha/2, 0, 1)
zright = -zleft  
print(zleft, zright)

# Make decision to reject hypothesis
print('At significant level of {}, shall we reject: {}'
      .format(alpha, zhat>zright or zhat<zleft))


# P value of two tail test 
p = 1 - norm.cdf(zhat, 0, 1)
print(p)
print('At significant level of {}, shall we reject: {}'
      .format(alpha, p < alpha))