import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
% matplotlib inline

fb = pd.DataFrame.from_csv('...data/facebook.csv')
fb.head()

fb['LogReturn'] = np.log(fb['Close']).shift(-1) - np.log(fb['Close'])

from scipy.stats import norm
mu = fb['LogReturn'].mean()
sigma = fb['LogReturn'].std(ddof=1)

density = pd.DataFrame()
density['x'] = np.arange(fb['LogReturn'].min()-0.01, fb['LogReturn'].max()+0.01, 0.001)
density['pdf'] = norm.pdf(density['x'], mu, sigma)

fb['LogReturn'].hist(bins=50)
plt.plot(density['x'], density['pdf'])
plt.show()

prob_return1 = norm.cdf(-0.05, mu, sigma)
prob_return2= norm.cdf(-0.1, mu, sigma)

mu220 = mu*220 # drop in 40% over 220 days
sigma220 = (220*0.5)*sigma 

VaR = norm.cdf(0.05, mu, sigma)
q25 = norm.ppf(0.25, mu, sigma)
q75 = norm.ppf(0.75, mu, sigma)


