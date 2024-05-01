# Given an integer numRows, return the first numRows of Pascal's triangle. 
# 
#  In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown: 
#  
#  
#  Example 1: 
#  Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#  
#  Example 2: 
#  Input: numRows = 1
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= numRows <= 30 
#  
# 
#  Related Topics Array Dynamic Programming 👍 12631 👎 431


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle_list = []
        row_count = 1
        for index in range(numRows):
            temp_list = []
            for item in range(row_count):
                if item == 0 or item == index:
                    temp_list.append(1)
                else:
                    temp_cal = triangle_list[index-1][item] + triangle_list[index-1][item-1]
                    temp_list.append(temp_cal)
            triangle_list.append(temp_list)
            row_count += 1
        return triangle_list
# leetcode submit region end(Prohibit modification and deletion)
