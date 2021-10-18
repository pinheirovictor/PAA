import numpy as np 
import matplotlib.pyplot as plt

x = np.array([24, 25, 26, 27, 28, 29, 30])
y = np.array([1.5196905136108398,
              2.987525224685669,
              5.919523239135742,
              12.441267251968384,
              24.833341121673584,
              47.445162534713745,
              94.58348202705383])


lx = x
ly = np.log2(y)

#plt.scatter(x, ly)
#plt.show()

#regressão linear, tranformar a curva do gráfico em uma reta a partir de um certo ponto
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