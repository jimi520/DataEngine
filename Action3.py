import pandas as pd
import numpy as np
 
df = pd.read_csv('.\\car_complain.csv', encoding = 'utf-8')

#对problem进行分多列
df1 = df.problem.str.get_dummies(',')

#删除problem列
df = df.drop(columns = 'problem')

#生产problem类型多字段
df_new = pd.concat([df,df1])

#print(df_new)
new_names = df_new.columns[7:]

#按brand分组，统计problem数量
df2 = df_new.groupby('brand')['id'].agg(['count']).sort_values('brand', ascending=False)

#按car_model分组，统计problem数量
df3 = df_new.groupby('car_model')['id'].agg(['count'])

#按brand分组，统计每个car_model数量
df4 = df_new.groupby(['brand','car_model'])['car_model'].agg(['count'])

#算出每个brand，problem的总数
sum_problem = df4.groupby(['brand'])['count'].sum().reset_index().sort_values('brand', ascending=False).iloc[:,1]

#算出brand，拥有car_model的数量
count_car_model = df4.groupby(['brand']).count().reset_index().sort_values('brand', ascending=False).iloc[:,1]

#计算平均值
avg = sum_problem/count_car_model
df2['平均车型投诉'] = list(avg)
#print(df2)

#打印结果,保留小数位2位
result = df2.sort_values('平均车型投诉', ascending=False).round(2)
print(result)
print('平均车型投诉最多的品牌是：{}，平均投诉量为：{}'.format(result.index[0],result.iloc[0,1]))

#result.to_csv('result.csv')
