import math
num = float(input("Entre com um número:\n"))
raiz = math.sqrt(num)
print(f'\nA raiz quadrada de {num} é {raiz}\n')


from sklearn.linear_model import LinearRegression
model = LinearRegression().fit(lx.reshape(-1, 1), ly)
print(('slope:', model.coef_))

plt.scatter(lx, ly)
plt.plot(lx, model.intercept_ + model.coef_ * lx, 'r')
plt.show()