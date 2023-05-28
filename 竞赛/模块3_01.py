"""
1、程序接收 DataFrame 对象df，返回结果是list数据类型
2、平均值需要四舍五入保留两位小数
"""

import numpy as np
import pandas as pd

class Solution:
	def CalAvg(self, df: 'pandas.DataFrame') -> list:
		# DataFrame对象添加新列直接赋值就可以
		# axis=0 表示从左到右
		# axis=1 表示从上到下
		df['avg'] = df.mean(axis=1).round(2)
		return df['avg'].tolist()


df = np.arange(100).reshape(10, 10)
df = pd.DataFrame(df)
print(Solution().CalAvg(df))