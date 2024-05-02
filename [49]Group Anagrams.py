# Given an array of strings strs, group the anagrams together. You can return 
# the answer in any order. 
# 
#  An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once. 
# 
#  
#  Example 1: 
#  Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#  
#  Example 2: 
#  Input: strs = [""]
# Output: [[""]]
#  
#  Example 3: 
#  Input: strs = ["a"]
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 10⁴ 
#  0 <= strs[i].length <= 100 
#  strs[i] consists of lowercase English letters. 
#  
# 
#  Related Topics Array Hash Table String Sorting 👍 18904 👎 601


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        final_dic = defaultdict(list)
        for st in strs:
            sort_st = ''.join(sorted(st))
            final_dic[sort_st].append(st)
        return list(final_dic.values())
# leetcode submit region end(Prohibit modification and deletion)
