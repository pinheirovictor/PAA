import numpy as np 
import matplotlib.pyplot as plt

x = np.array([800, 1600, 3200, 6400, 12800, 25600, 51200])
y = np.array([0.049222707748413086,
              0.049222707748413086,
              0.7536275386810303,
              3.0468943119049072,
              12.811365127563477,
              68.55198884010315,
              236.31884241104126])

lx = np.log2(x)
ly = np.log2(y)

# regressão linear, tranformar a curva do gráfico em uma reta a partir de um certo ponto
from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(lx.reshape(-1, 1), ly)
print('slope:', model.coef_)

plt.scatter(lx, ly)
plt.plot(lx, model.intercept_ + model.coef_ * lx, 'r')
plt.show()

# intervalo de confiança, grau do polinomio
import statsmodels.api as sm
lx = sm.add_constant(lx)
res = sm.OLS(ly, lx).fit()
print('slope conf interval:', res.conf_int(0.05)[1])