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
            
            while not s[i + j].isalnum() and not (i+j >= len(s)-j):
                j+=1
            while not s[len(s) - i - 1 - x].isalnum() and not len(s) - i - 1 - x < 0:
                x+=1

            print(s[i+j].lower(), s[len(s) - i - 1 - x].lower())
            if s[i + j].lower() != s[len(s) - i - 1 - x].lower():
                return False
        return True 