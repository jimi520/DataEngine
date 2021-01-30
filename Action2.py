import pandas as pd
import numpy as np

#数据源,组成DataFrame
data = {'语文':[68,95,98,90,80],
        '数学':[65,76,86,88,90],
        '英语':[30,98,88,77,90]}
index = ['张飞','关羽','刘备','典韦','许褚']
df = pd.DataFrame(data, index)

#统计平均成绩、最小成绩、最大成绩、标准差
result = df.describe()
result = result.drop(index = ['count','25%','50%','75%'])
#保留2玮小数点
result.round(2)
print(result)

#统计方差
var =df.var()
print('各科成绩的方差为：\n',var)

#总成绩
total_score = df.sum(axis=1).sort_values(ascending = False)

#输出各科统计结果
for i in range(len(df.columns)):
    print('{}:\n平均成绩{:.2f}\n最小成绩{:.0f}\n最大成绩{:.0f}\n方差{:.2f}\n标准差{:.2f}'.format(df.columns[i], result.iloc[0,i], result.iloc[2,i], result.iloc[3,i], list(var)[i], result.iloc[1,i]),end = '\n')
    

#输出成绩排名情况
print('总成绩排名情况：')
for i in range(len(total_score)):
    print('第{}名：{}，总分：{}'.format(i+1,total_score.index[i], total_score.values[i]))

