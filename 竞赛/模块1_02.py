"""
1、对于任意输入的一个整数数组，如果整数数组中存在重复元素且重复元素均不相邻，函数返回 字符"01"
2、整数数组每个元素均不相同且偶数元素个数大于奇数元素个数，函数返回字符"02"
3、整数数组均不满足上述两个条件，函数返回字符 "03"
4、函数接收一个变量 arr，list 数据类型
5、函数返回值必须为字符串数据类型
"""

class Solution:
    
    def arrayRepeat(self, arr: list) -> str:
        flag = False  # 条件1
        even_number = 0  # 偶数
        uneven_number = 0  # 奇数
        n = len(arr)  # 列表元素个数
        for i in range(n):
            # 分别记录奇数偶数的个数
            if arr[i] % 2 == 0:
                even_number += 1
            else:
                uneven_number += 1

            # 判断是否有重复元素，并控制索引
            if arr.count(arr[i]) > 1 and i < n - 1:
                # 判断重复元素是否为不相邻元素
                if arr[i] == arr[i + 1]:
                    return "03"
                else:
                    flag = True
        
        # 判断两个条件
        if flag:
            return "01"
        elif (not flag) and (even_number > uneven_number):
            return "02"
        else:
            return "03"

       
        pass


print(Solution().arrayRepeat([2, 0, 2, 5, 5]))