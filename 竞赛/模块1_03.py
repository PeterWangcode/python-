"""
编写Python程序计算下列数学表达式的结果并输出，结果向上取整保留整数。
res = √(( 3 ^ 4 + 5 * 6 ^ 5) / num)
程序接收变量 num，返回的是 res。
"""

import math


class Solution:

    def SpMtFml(self, num: int) -> int:
	    res = math.ceil(pow((3 ** 4 + 5 * 6 ** 5) / num, 0.5))
	    return res
	    
	    pass