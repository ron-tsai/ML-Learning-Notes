
#第一步：调用pandas包
import pandas as pd
#第二步：读取数据
io=r'C:\Users\Administrator\Desktop\data\S5\S5_train_data.xlsx'
##表格1
iris1 = pd.read_excel(io,header=None,sheet_name=0)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=0

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_1_train_data.xlsx')#数据保存路径

##表格2

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=1

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_2_train_data.xlsx')#数据保存路径

##表格3

iris1 = pd.read_excel(io,header=None,sheet_name=2)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=2

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_3_train_data.xlsx')#数据保存路径

##表格4

iris1 = pd.read_excel(io,header=None,sheet_name=3)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=3

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_4_train_data.xlsx')#数据保存路径


##表格5

iris1 = pd.read_excel(io,header=None,sheet_name=4)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=4

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_5_train_data.xlsx')#数据保存路径

##表格6

iris1 = pd.read_excel(io,header=None,sheet_name=5)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=5

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_6_train_data.xlsx')#数据保存路径

##表格7

iris1 = pd.read_excel(io,header=None,sheet_name=6)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=6

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_7_train_data.xlsx')#数据保存路径


##表格8

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=7

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_8_train_data.xlsx')#数据保存路径


##表格9

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=8

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_9_train_data.xlsx')#数据保存路径


##表格10

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=9

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_10_train_data.xlsx')#数据保存路径


##表格11

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=10

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_11_train_data.xlsx')#数据保存路径


##表格12

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']=11

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S5\\train_data_label\\5_12_train_data.xlsx')#数据保存路径


