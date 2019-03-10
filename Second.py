import pandas as pd

df = pd.read_csv('HKEX-83079.csv')
print(df.head())

df.set_index('Date', inplace=True)
df.to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())
# 两次输出结果相同，原因在于 CSV 文件没有 index 属性

df = pd.read_csv('newcsv2.csv', index_col=0) # 所以需要在读取的时候，直接设定 index 列
print(df.head())

# 改变列名称，注意 index 列并属于列
df.columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
print(df.head())

# 存储时若不需要列名称
df.to_csv('newcsv3.csv', header=False)

# 在读取时添加列名称
df = pd.read_csv('newcsv3.csv', names=['Date', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], index_col=0)
print(df.head())

# 转换成 html
df.to_html('example.html')

# 重命名, 注意需要加 inplace ，不然不会对 df 进行修改
df.rename(columns = {'1': 'PRICES'}, inplace=True)
print(df.head())