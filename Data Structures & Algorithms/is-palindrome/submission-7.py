class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        j = 0
        x = 0
        for i in range(len(s)):
            print (i + j, "compared to", len(s) - i - 1 - x)
            if (i + j > len(s) - i - 1 - x) or (i+j >= len(s)-j) or len(s) - i - 1 - x < 0:
                print("reached")
                return True
            
            while not self.alphaNum(s[i + j]) and not (i+j >= len(s)-j):
                j+=1
            while not self.alphaNum(s[len(s) - i - 1 - x]) and not len(s) - i - 1 - x < 0:
                x+=1

            print(s[i+j].lower(), s[len(s) - i - 1 - x].lower())
            if s[i + j].lower() != s[len(s) - i - 1 - x].lower():
                return False
        return True 
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))