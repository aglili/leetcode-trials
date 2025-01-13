# Day 2
# 13th january 24



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """
        Merge two strings alternately, character by character. 
        After exhausting one string, append the remaining characters from the other string.
        
        Time Complexity: O(n) where n is max length of word1 and word2
        Space Complexity: O(n) for storing the merged string
        
        Args:
            word1 (str): First input string
            word2 (str): Second input string
            
        Returns:
            str: Merged string with characters from both words alternately
            
        Examples:
            >>> sol = Solution()
            >>> sol.mergeAlternately("abc", "pqr")
            "apbqcr"
            >>> sol.mergeAlternately("ab", "pqrs")
            "apbqrs"
            >>> sol.mergeAlternately("abcd", "pq")
            "apbqcd"
            
        Note:
            - First character in result always comes from word1
            - Continue alternating until one string is exhausted
            - Append remaining characters from longer string at the end
        """
        A, B = len(word1), len(word2)
        a, b = 0, 0
        s = []
        
        # Alternate between words until one is exhausted
        while a < A and b < B:
            s.append(word1[a])
            s.append(word2[b])
            a += 1
            b += 1
        
        # Append remaining characters from word1 if any
        while a < A:
            s.append(word1[a])
            a += 1
            
        # Append remaining characters from word2 if any
        while b < B:
            s.append(word2[b])
            b += 1
            
        return "".join(s)

        
        


            
