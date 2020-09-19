import pandas as pd
import os
files=[file for file in os.listdir('C:\\Users\Administrator\Desktop\data\S4\\train_data_label')]
print(files)
all_goods=pd.DataFrame()
for file in files:
    df=pd.read_excel('C:\\Users\Administrator\Desktop\data\S4\\train_data_label\\'+file)
    all_goods=pd.concat([all_goods,df])
# print(all_goods)
all_goods.to_excel('C:\\Users\Administrator\Desktop\data\S4\\combine_4_train_data.xlsx')