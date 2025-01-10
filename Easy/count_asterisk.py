# Day 2
# 10th january 24



class Solution:
   def countAsterisks(self, s: str) -> int:
       """
       Count the number of asterisks (*) in string s, excluding those between pairs of vertical bars (|).
       
       Time Complexity: O(n) where n is length of string s
       Space Complexity: O(n) for storing split segments
       
       Args:
           s (str): Input string containing asterisks and vertical bars
           
       Returns:
           int: Count of asterisks not between vertical bar pairs
           
       Examples:
           >>> sol = Solution()
           >>> sol.countAsterisks("l|*e*et|c**o|*de|")
           2
           >>> sol.countAsterisks("yo|uar|e**|b|e***au|tifu|l")
           5
           >>> sol.countAsterisks("string")
           0
           
       Note:
           - Vertical bars always come in pairs
           - Only count asterisks in segments not between a pair of bars 
           - Empty string returns 0
       """
       # Split string by vertical bars
       segments = s.split("|")
  
       # Only count asterisks in even-indexed segments
       # (segments not between bar pairs)
       count = 0
       for i in range(0, len(segments), 2):
           count += segments[i].count("*")
           
       return count
   