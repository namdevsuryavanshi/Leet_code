# Palindrome Number

# An integer is a palindrome when it reads the same forward and backward.

class Solution :
    def pare1(self , x:int) -> bool:
        s1 = str(x)
        reversedstring = ""
        for i in s1 :
            reversedstring = i + reversedstring

        if reversedstring == s1:
            return  True
        else:
            return  False

