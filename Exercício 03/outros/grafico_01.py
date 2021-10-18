import numpy as np 
import matplotlib.pyplot as plt

x = np.array([25, 50, 100, 200, 400, 800, 1600])
y = np.array([0.0038008689880371094,
              0.008645296096801758,
             0.027943849563598633,
              0.23390960693359375,
              3.5526700019836426,
              16.36064624786377,
              130.45713257789612])

lx = np.log2(x)
ly = np.log2(y)


from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(lx.reshape(-1, 1), ly)
print('slope:', model.coef_)

plt.scatter(lx, ly)
plt.plot(lx, model.intercept_ + model.coef_ * lx, 'r')
plt.show()

import statsmodels.api as sm

lx = sm.add_constant(lx)
res = sm.OLS(ly, lx).fit()
print('slope conf interva:', res.conf_int(0.05)[1])