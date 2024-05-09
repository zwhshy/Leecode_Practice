# Given two strings s and t, determine if they are isomorphic. 
# 
#  Two strings s and t are isomorphic if the characters in s can be replaced to 
# get t. 
# 
#  All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the same 
# character, but a character may map to itself. 
# 
#  
#  Example 1: 
#  Input: s = "egg", t = "add"
# Output: true
#  
#  Example 2: 
#  Input: s = "foo", t = "bar"
# Output: false
#  
#  Example 3: 
#  Input: s = "paper", t = "title"
# Output: true
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 5 * 10⁴ 
#  t.length == s.length 
#  s and t consist of any valid ascii character. 
#  
# 
#  Related Topics Hash Table String 👍 8851 👎 2052


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        word_dic = {}
        count = 0
        word_list = []
        new_word_dic = {}
        new_count = 0
        new_word_list = []
        for word, new_word in zip(s, t):
            if word not in word_dic:
                count += 1
                word_dic[word] = count
                word_list.append(count)
            else:
                old_word_index = word_dic[word]
                word_list.append(old_word_index)
            if new_word not in new_word_dic:
                new_count += 1
                new_word_dic[new_word] = new_count
                new_word_list.append(new_count)
            else:
                new_old_word_index = new_word_dic[new_word]
                new_word_list.append(new_old_word_index)
            if word_list != new_word_list:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)
