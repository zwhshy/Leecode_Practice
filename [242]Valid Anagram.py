# Given two strings s and t, return true if t is an anagram of s, and false 
# otherwise. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: s = "anagram", t = "nagaram"
# Output: true
#  
#  Example 2: 
#  Input: s = "rat", t = "car"
# Output: false
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length, t.length <= 5 * 10⁴ 
#  s and t consist of lowercase English letters. 
#  
# 
#  
#  Follow up: What if the inputs contain Unicode characters? How would you 
# adapt your solution to such a case? 
# 
#  Related Topics Hash Table String Sorting 👍 11913 👎 394


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        word_count = {}
        for word in s:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for word in t:
            if word in word_count:
                if word_count[word] > 0:
                    word_count[word] -= 1
                else:
                    return False
            else:
                return False
        all_zero = all(value == 0 for value in word_count.values())
        if all_zero:
            return True
        else:
            return False
# leetcode submit region end(Prohibit modification and deletion)
