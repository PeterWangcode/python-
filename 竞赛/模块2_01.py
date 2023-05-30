"""
- 任务详情
	给定一个由表格构成的网页，返回指定位置中的数字，数字类型要转换为 int 类型。
	后台给出指定位置，位置由行（row）和列（col）构成，如 row = 2, col = 1, 表示第二行第一列，对应的数字是 249；
	程序返回的数字必须是 int 类型，类型不正确将导致结果不正确；
	后台给出的所有的位置都在表格中，无需考虑边界情况；
	表格的第一行是列名，由 A-Z 构成，共 26 列；第一列是行索引，由 1-30 构成，共 30 行。
- 任务要求
	程序给出 int 类型的参数 row 和 col；
	程序返回参数是 int 类型。
- 测试用例
	输入：row=29, col=20
	输出：252
	解释：表格第 29 行第 20 列中的数字是 252
"""

import requests
from bs4 import BeautifulSoup


class Solution:

    def table_num(self, row: int, col: int) -> int:
    	url = r'http://72.itmc.org.cn/JS001/open/show/random-num/index.html'
    	reasponse = requests.get(url)
    	reasponse.encoding = 'UTF-8'

    	soup = BeautifulSoup(reasponse.text, 'lxml')
    	elements = soup.select(
    		f'body > table > tbody:nth-child(2) > tr:nth-child({row}) > td:nth-child({col + 1})'
    		)
    	print(elements[0].text)

    	pass


Solution().table_num(10, 11)