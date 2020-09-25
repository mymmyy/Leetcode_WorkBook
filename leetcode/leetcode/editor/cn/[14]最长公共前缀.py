# 编写一个函数来查找字符串数组中的最长公共前缀。 
# 
#  如果不存在公共前缀，返回空字符串 ""。 
# 
#  示例 1: 
# 
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#  
# 
#  示例 2: 
# 
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#  
# 
#  说明: 
# 
#  所有输入只包含小写字母 a-z 。 
#  Related Topics 字符串 
#  👍 1282 👎 0
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        if len(strs) <= 0:
            return ""
        first_deep = -1
        while True:
            first_deep += 1
            if len(strs[0]) <= first_deep:
                break
            cur_deep_str = strs[0][first_deep]
            cur_deep_str = self.recusion(strs, 0, first_deep, cur_deep_str)
            if cur_deep_str == "":
                break
            result += cur_deep_str
        return result

    def recusion(self, strs: List[str], index: int, deep: int, cur_str: str) -> str:
        if cur_str == "":
            return ""
        while index < len(strs):
            if strs[index] == "" or deep >= len(strs[index]):
                return ""
            if cur_str == strs[index][deep]:
                return self.recusion(strs, index + 1, deep, cur_str)
            else:
                return ""

        return cur_str
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':

    s = Solution()
    result = s.longestCommonPrefix(["aca", "bda"])
    print(result)