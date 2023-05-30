import re

import requests
from bs4 import BeautifulSoup


class Solution:
    def itemSearch(self, shop_name: str) -> list:
        url = 'http://72.itmc.org.cn/JS001/open/show/ecjd.html'
        rep = requests.get(url)
        rep.encoding = 'UTF-8'
        soup = BeautifulSoup(rep.text, 'lxml')

        # 定位<li>标签
        for child in soup.find_all(class_='gl-item'):
            item_name = child.find(class_='J_im_icon').a.text  # 店铺名称
            price = float(child.find(class_='p-price').strong.i.text) # 价格
            # 若有VIP价格则替换为VIP价格
            if child.find(class_='p-price').span:
                price = float(child.find(class_='p-price').span.em.text[1:])
            comment = child.find(class_='p-commit').strong.a.text  # 评论
            comment = re.match(r'(\d\.\d+万\+)|(\d+\+)', comment)
            if comment:
                print(comment)




Solution().itemSearch("1")