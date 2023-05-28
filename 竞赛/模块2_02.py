"""
1. 构建函数 wordTfidf()，对商品中除停用词外的关键词，计算其TF-IDF值
2. 返回文本中 TF-IDF 最大的前5个关键词，返回结果为 list 数据类型
3. 只保留词性为 n、nr、ns 的关键词
4. 下方给出的文本编码为UTF-8
"""

import jieba
from jieba import analyse
import requests

class Solution:
    def wordTfidf(self) -> list:
    	flag_url = r'http://72.itmc.org.cn/JS001/static/data/python/3030/126/fj_chiffon_lady_dress.txt'  # 目标位置
    	stop_url = r'http://72.itmc.org.cn/JS001/static/data/python/3030/126/fj_cn_stopwords.txt'  # 停用词位置

    	respnose = requests.get(flag_url)
    	respnose.encoding = 'utf-8'  # 指定编码
    	flag_str = [s for s in respnose.text.splitlines()]
    	flag_str = "".join(flag_str)
    	flag_str = jieba.lcut(flag_str)

    	respnose = requests.get(stop_url)
    	respnose.encoding = 'utf-8'
    	stop_str = [st for st in respnose.text.splitlines()]
    	stop_str = "".join(stop_str)
    	stop_str = jieba.lcut(stop_str)

    	true_str = []
    	for i in flag_str:
    		if i not in stop_str:
    			true_str.append(i)

    	true = "".join(true_str)
    	return jieba.analyse.extract_tags(true, topK=5, allowPOS=('n', 'nr', 'ns'))


print(Solution().wordTfidf())