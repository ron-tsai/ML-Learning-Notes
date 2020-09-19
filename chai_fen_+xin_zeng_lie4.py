
#第一步：调用pandas包
import pandas as pd
#第二步：读取数据
io=r'C:\Users\Administrator\Desktop\data\S4\S4_train_data.xlsx'
##表格1
iris1 = pd.read_excel(io,header=None,sheet_name=0)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='B'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_1_train_data.xlsx')#数据保存路径

##表格2

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='D'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_2_train_data.xlsx')#数据保存路径

##表格3

iris1 = pd.read_excel(io,header=None,sheet_name=2)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='G'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_3_train_data.xlsx')#数据保存路径

##表格4

iris1 = pd.read_excel(io,header=None,sheet_name=3)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='L'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_4_train_data.xlsx')#数据保存路径


##表格5

iris1 = pd.read_excel(io,header=None,sheet_name=4)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='O'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_5_train_data.xlsx')#数据保存路径

##表格6

iris1 = pd.read_excel(io,header=None,sheet_name=5)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='Q'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_6_train_data.xlsx')#数据保存路径

##表格7

iris1 = pd.read_excel(io,header=None,sheet_name=6)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='S'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_7_train_data.xlsx')#数据保存路径


##表格8

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='V'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_8_train_data.xlsx')#数据保存路径


##表格9

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='Z'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_9_train_data.xlsx')#数据保存路径


##表格10

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='4'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_10_train_data.xlsx')#数据保存路径


##表格11

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='7'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_11_train_data.xlsx')#数据保存路径


##表格12

iris1 = pd.read_excel(io,header=None,sheet_name=1)#读入数据文件关键中的关键：header=None


iris1.loc[:,'label']='9'

iris1.to_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\4_12_train_data.xlsx')#数据保存路径


