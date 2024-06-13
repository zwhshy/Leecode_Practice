# You have a long flowerbed in which some of the plots are planted, and some 
# are not. However, flowers cannot be planted in adjacent plots. 
# 
#  Given an integer array flowerbed containing 0's and 1's, where 0 means empty 
# and 1 means not empty, and an integer n, return true if n new flowers can be 
# planted in the flowerbed without violating the no-adjacent-flowers rule and false 
# otherwise. 
# 
#  
#  Example 1: 
#  Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
#  
#  Example 2: 
#  Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= flowerbed.length <= 2 * 10⁴ 
#  flowerbed[i] is 0 or 1. 
#  There are no two adjacent flowers in flowerbed. 
#  0 <= n <= flowerbed.length 
#  
# 
#  Related Topics Array Greedy 👍 6464 👎 1156


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowercount = 0
        new_flowerbed = [0] + flowerbed + [0]
        for index in range(1, len(new_flowerbed) - 1):
            prev, after = new_flowerbed[index - 1], new_flowerbed[index + 1]
            curr = new_flowerbed[index]
            if curr == 0 and prev == 0 and after == 0:
                flowercount += 1
                new_flowerbed[index] = 1
        if flowercount >= n:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
