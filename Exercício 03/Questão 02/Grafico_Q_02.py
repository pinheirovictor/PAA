import numpy as np 
import matplotlib.pyplot as plt

x = np.array([51200, 102400, 204800, 409600, 819200, 1638400, 3276800])
y = np.array([0.2754955291748047,
              0.5294005870819092,
              1.31569504737854,
              2.6674180030822754,
              5.5848917961120605,
              17.545719146728516,
              26.77403974533081])


lx = np.log2(x)
ly = np.log2(y)

#plt.scatter(lx, ly)
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