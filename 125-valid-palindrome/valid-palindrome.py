class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        newStr = ""
        for i in s:
            if i.isalnum():
                newStr += i.lower()
        i, j = 0, len(newStr) - 1
        
        while i<j:
            if newStr[i] == newStr[j]:
                i+=1
                j-=1
            else:
                return False
        return True
