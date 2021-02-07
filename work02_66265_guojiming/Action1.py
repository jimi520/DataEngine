import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_url_con(url):
    #url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml'

    #？？？headers变量怎么来的？？？，还请老师解惑
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(url, headers = headers ,timeout = 20)
    content = html.text
    #生产BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding = 'utf-8')
    return soup


def get_df(soup):
    #获取表格整页内容
    result_table = soup.find('div', class_='tslb_b')
    columns = ['投诉编号','投诉品牌','投诉车系','投诉车型','问题简述','典型问题','投诉时间','投诉状态']
    df = pd.DataFrame(columns = columns)
    #获取表格内‘tr’开头数据
    tr_list = result_table.find_all('tr')
    for i in tr_list:
        #获取表格内‘td’开头数据，去除表头，并转换成文本
        td_list = i.find_all('td')
        if len(td_list) > 0:
            id, brand, model, type, details, problem, datetime, sta = [td_list[x].text for x in range(8)]
            temp = {}
            temp['投诉编号'] = id
            temp['投诉品牌'] = brand
            temp['投诉车系'] = model
            temp['投诉车型'] = type
            temp['问题简述'] = details
            temp['典型问题'] = problem
            temp['投诉时间'] = datetime
            temp['投诉状态'] = sta                    
            df = df.append(temp, ignore_index=True)
    return df

result = pd.DataFrame(columns = ['投诉编号','投诉品牌','投诉车系','投诉车型','问题简述','典型问题','投诉时间','投诉状态'])
url_base = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0'
#input_page_num = int(input('请输入需要爬取的页数：'))
#确定需要爬取的页数
input_page_num = 10
for i in range(input_page_num):
    #拼接url
    url = url_base + str(i+1) + '.shtml'
    soup = get_url_con(url)
    df = get_df(soup)
    result = result.append(df, ignore_index=True)
  
result.to_excel('car_complain.xlsx',index=False)
print('文件存储完成')

