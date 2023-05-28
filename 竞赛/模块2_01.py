import requests
from bs4 import BeautifulSoup
import re

class Solution:
	def weixinData(self, name: str) -> str:
		url = 'http://72.itmc.org.cn/JS001/open/show/weixindata.html'
		respnose = requests.get(url)
		respnose.encoding = 'utf-8'
		soup = BeautifulSoup(respnose.text, "html.parser")
		elements = soup.tbody.find_all("tr")

		information_list = []
		for element in elements:
			dct = {}
			name_ = element.find("span", {'class': 'js-rank-detail-btn'}).get_text()  # 公众号名称
			top_line = element.find_all('td')[4].get_text()  # 头条平均阅读数
			original_read = element.find_all('td')[7].get_text()  # 原创平均阅读
			fans_number = element.find_all('td')[3].get_text()  # 预估活跃粉丝

			dct = {
					"公众号名称": name_,
					"头条平均阅读数": top_line,
					"原创平均阅读": original_read,
					"预估活跃粉丝": fans_number
					}

			information_list.append(dct)

		# 遍历列表，对比公众号名称
		for data in information_list:
			if data.get("公众号名称") == name:
				top_line = data.get("头条平均阅读数").replace("万+", "0000")
				original_read = data.get("原创平均阅读").replace("万+", "0000")
				fans_number = data.get("预估活跃粉丝").replace("万", "")
				# 查看该公众号是否满足要求
				if float(top_line) > 90000 and float(original_read) > 80000 and float(fans_number) < 300:
					return "Yes"
				else:
					return "No"


print(Solution().weixinData("广东共青团"))