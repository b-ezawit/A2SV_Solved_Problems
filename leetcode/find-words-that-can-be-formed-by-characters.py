class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        charsCount = Counter(chars) 
        ans = 0
        for string in words:
            stringCount = Counter(string)
            for ch in stringCount:
                if (stringCount[ch] > charsCount[ch]):
                    break
            else:
                ans += len(string)
        return ans

            
