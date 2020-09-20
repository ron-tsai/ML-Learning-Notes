import pandas as pd
import os
files=[file for file in os.listdir('C:\\Users\Administrator\Desktop\data\evetually_train')]
print(files)
all_goods=pd.DataFrame()
for file in files:
    df=pd.read_excel('C:\\Users\Administrator\Desktop\data\evetually_train\\'+file)
    all_goods=pd.concat([all_goods,df])
# print(all_goods)
all_goods.to_excel('C:\\Users\Administrator\Desktop\data\\total_train.xlsx')