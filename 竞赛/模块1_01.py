"""
1. 代码编写必须在右边指定的区域编写；
2. 函数接收两个变量，一个是整数数组 nums：list，另一个是目标值 target: int；
3. 如果存在两种或以上符合目标值 target 的情况，返回下标相加之和较小的数组；
4. 函数返组，回的值必须为一个数list数据类型，元素排序为正序排序，如返回 [1, 3] 符合条件，[3, 1] 不符合条件。
"""

class SearchIndex:
	def searchIndex(self, nums: list, target: int) -> list:
		n = len(nums)  # 计算数组cahngdu
		for i in range(n):
			for j in range(1, n - 1):
				if nums[i] + nums[j] == target:
					return [j, i] if i > j else [i, j]
		return []


index = SearchIndex().searchIndex([2, 1, 6, 8, 5, 1, 2, 4, 5, 2, 4, 5, 17, 10], 27)
print(index)