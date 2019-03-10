import quandl
import pandas as pd

# # 添加 api 密码
# api_key = 'RsstDDb5Lbfdrvyuu93y'
# # 从 quandl 上获取
# df = quandl.get('FMAC/HPI_49700', authtoken = api_key)

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# # 这是由 DataFrame 组成的 list
# print(fiddy_states)

# 这是第一个 DataFrame
# print(fiddy_states[0])

# 这是第一个 DataFrame 的第一列
# print(fiddy_states[0][0])

# 将第 2 列按照要求输出
for abbv in fiddy_states[0][1][1: ]:
    print("FMAC/HPI_" + str(abbv))