
#第一步：调用pandas包
import pandas as pd

#第二步：读取数据
io=r'C:\Users\Administrator\Desktop\data\S1\S1_train_data.xlsx'
iris = pd.read_excel(io,header=None)#读入数据文件关键中的关键：header=None
keys = list(iris.keys())

# 第三步：数据合并
iris_concat = pd.DataFrame()

for i in keys:
    iris1 = iris[i]
    iris_concat = pd.concat([iris_concat,iris1])
iris_concat.to_excel('C:\\Users\Administrator\Desktop\data\S1\\1_train_data.xlsx')#数据保存路径




