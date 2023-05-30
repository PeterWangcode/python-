"""
给定内地某日票房排行榜，输入指定影片名称 movie_name，如：'金刚川'。完成以下任务：

1. 任务一：获取指定影片的上映天数。如“金刚川”上映20天，返回 20；“一日成交”上映首日，返回0，“翱翔雄心”点映，返回 -1；

2. 任务二：获取指定影片的综合票房（万元）。如“金刚川”，返回 432.33；

3. 任务三：获取指定影片的排片占比。如“金刚川”，返回 0.248。
"""

import re
import bs4
import requests

class Solution:
    def BoxOfficeSpider(self, movie_name: str) -> list:
        url = r'http://72.itmc.org.cn/JS001/open/show/box_office_on_a_certain_day.html'
        res = requests.get(url)
        res.encoding = 'utf-8'

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        rw1 = rw2 = rw3 = 0  # 上映天数、返回票房、排片占比

        for element in soup.find_all('tr', class_='body-row'):
            name = element.find('p', class_='movie-name').text.strip()  # 名称
            if movie_name == name: 
                view_time = element.find('span', class_='releaseInfo').text.strip()  # 上映时间
                if '首日' in view_time:
                    rw1 = 0
                elif '点映' in view_time:
                    rw1 = -1
                else:
                    rw1 = int(re.match(r'上映(\d+)天', view_time).group(1))

                piaofang = element.find('div', class_='red-color').text  # 票房
                rw2 = float(piaofang)

                paipian = element.find('div', class_='countRate-wrap').text[:-1]  # 排片占比
                if '<' in paipian:
                    rw3 = 0.001
                else:
                    rw3 = float(paipian) / 100

                return [rw1, rw2, round(rw3, len(paipian))]
        pass


print(Solution().BoxOfficeSpider("一日成交"))
# re_1 = int(re.match('上映(\d+)天', releaseInfo).group(1))