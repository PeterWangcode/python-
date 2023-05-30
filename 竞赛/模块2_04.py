"""
1. 不得直接使用 Jieba 库对文本进行分词；

2. 函数 aliceText() 接收一个英文单词 word，str 数据类型；返回该单词的词频，int 数据类型；

3. 只保留单词长度大于等于 3 的单词的词频统计；

4. 英文单词不区分大小写；

5. 不同时态和单复数的英文单词为不同英文单词，不需要合并词频统计。如果文本中没有该单词，词频为0；

6. 文本可以使用 requests 库进行读取，UTF-8 编码方式，否则无法正确读取文本。
"""

import re

import requests
from collections import Counter

class Solution:
    def aliceText(self, word: str) -> int:
        url = r'http://72.itmc.org.cn:80/JS001/data/user/14834/76/fj_alice_adventure.txt'
        res = requests.get(url)
        res.encoding = 'utf-8'
        # re.sub(正则模式，替换成的字符，数据源)
        text = re.sub('[^A-Za-z1-9\']', ' ', res.text).replace('\n', ' ')

        # 创建空字典
        word_dict = dict()
        for wo in text.split():
            # 将单词都转换为小写
            wo = wo.lower()
            # 只统计单词长度大于三的
            if len(word) > 3:
                word_dict[wo] = word_dict.get(wo, 0) + 1

        return word_dict.get(word.lower(), 0)
        pass


print(Solution().aliceText("Pictures"))
print(Solution().aliceText("nothing"))
print(Solution().aliceText("caterpillar"))
print(Solution().aliceText("python"))

