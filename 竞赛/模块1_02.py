"""
除以下特殊情况外，句子中第一个单词首字母必须大写，其它所有单词小写：
1. 如果句中的某个单词或短语，字母全部为大写，则该单词或短语拼写正确。比如“USA”、“UK”、“JUST DO IT”等；
2. “Python”、“Java”、“MachineLearning”、“DataMining”四个单词必须为双引号中给出的形式，否则拼写不正确；
3. 如果句中单词为“数字+字母”的混合形式，比如“5G”，该单词所有字母全部大写。
"""

import re


class JudgeStr:
    def judge_str(self, string: str) -> bool:
        str_list = string.split()  # 以空格为分隔符，将字符串分隔
        true_list = ["Python", "Java", "MachineLearning", "DataMining"]  # 特殊字符

        # 判断首单词的首字母是否大写或首单词的全部字母大写
        if str_list[0].istitle() or str_list[0].isupper():
            # 首单词的首字母大写且不是特殊字符
            if str_list[0] in ['Machinelearning', 'Datamining']:
                return False
        else:
            # 若首单词没大写，也不是特殊字符，不符合规则
            if str_list[0] not in true_list:
                return False

        # 判断除首单词外的其他字符
        for word in str_list[1:]:
            # 判断其是否在特殊字母中
            if word.lower() in [s.lower() for s in true_list]:
                # 若在特殊单词中，判断其是否符合规范
                if word not in true_list:
                    continue

            # 判断其是否含有数字
            if re.search(r'(\d)|([A-Z])', word):
                # 判读包含数字的单词中，其他字母是否大写
                if word not in true_list:
                    if not (word == word.upper()):
                        return False

        return True


print(JudgeStr().judge_str("I love Python"))
print(JudgeStr().judge_str("python love me"))
print(JudgeStr().judge_str("JUST DO IT"))
print(JudgeStr().judge_str("I come from HK"))
print(JudgeStr().judge_str('Machinelearning is so hot'))


