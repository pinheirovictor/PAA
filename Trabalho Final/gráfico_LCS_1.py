import numpy as np 
import matplotlib.pyplot as plt

x = np.array([41, 42, 43, 44, 45, 46])
y = np.array([21.679840326309204,
              84.8117344379425,
              99.80419635772705,
              148.0605926513672,
              154.82751893997192,
              423.7757546901703])

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