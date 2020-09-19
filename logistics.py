import random
import matplotlib.pyplot as plt
import numpy as np

x, y = [], []
x_test1, x_test2, x_test3 = [], [], []

# 随机生成3种不同分类的点，分别打上标签存在y中
for i in range(0, 20):
    x1 = random.random()
    x2 = random.random()
    if x1 + x2 < 1:
        x.append([x1, x2, 1])
        x_test1.append([x1, x2])
        y.append([1, 0, 0])

    x.append([x1 * 2, x2 + 1, 1])
    x_test2.append([x1 * 2, x2 + 1])
    y.append([0, 1, 0])

    if x1 > x2:
        x.append([x1 + 1, x2, 1])
        x_test3.append([x1 + 1, x2])
        y.append([0, 0, 1])

# 将list转换为numpy array
x = np.array(x)
y = np.array(y)

# 学习率
lr = 0.5

w = np.ones((3, 3))
m = len(x)
for i in range(0, 1000):
    w_gard = 0
    for j in range(0, m):
        # sigmoid函数分类，这里用到了矩阵乘法
        w_gard += -x[j] * np.atleast_2d(1 / (1 + np.exp(-np.matmul(w, x[j]))) - y[j]).T
    w += lr * w_gard / m

# 画点
plt.plot(np.array(x_test1)[:, 0], np.array(x_test1)[:, 1], 'ro')
plt.plot(np.array(x_test2)[:, 0], np.array(x_test2)[:, 1], 'gx')
plt.plot(np.array(x_test3)[:, 0], np.array(x_test3)[:, 1], 'b.')
# 画分类直线
plt.plot([0, 2], [-w[0][2] / w[0][1], -(w[0][2] + 2 * w[0][0]) / w[0][1]], 'r')
plt.plot([0, 2], [-w[1][2] / w[1][1], -(w[1][2] + 2 * w[1][0]) / w[1][1]], 'g')
plt.plot([0, 2], [-w[2][2] / w[2][1], -(w[2][2] + 2 * w[2][0]) / w[2][1]], 'b')

plt.show()