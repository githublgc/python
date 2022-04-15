import numpy as np
from sklearn import datasets,linear_model

# 定义训练数据
x = np.array([[100,4,9.3],[50,3,4.8],[100,4,8.9],
              [100,2,6.5],[50,2,4.2],[80,2,6.2],
              [75,3,7.4],[65,4,6],[90,3,7.6],[90,2,6.1]])
print(x)
X = x[:,:-1]
Y = x[:,-1]
print(X,Y)

# 训练数据
regr = linear_model.LinearRegression()
regr.fit(X,Y)
print('coefficients(b1,b2...):',regr.coef_)
print('intercept(b0):',regr.intercept_)

# 预测
x_test = np.array([[102,6],[100,4]])
y_test = regr.predict(x_test)
print(y_test)
