class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanindexdict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        counter = -1
        addromans = 0
        for i in s:
            counter = counter +1
            
            if counter == 0 or counter == ([len(s)]):
                romanlookup = romanindexdict[i]
                addromans = addromans + romanlookup
            else:
                withpreviousCHR = s[counter-1:counter+1]
                if withpreviousCHR == "IV" or withpreviousCHR == "IX" or withpreviousCHR == "XL" or withpreviousCHR == "XC" or withpreviousCHR == "CD" or withpreviousCHR == "CM":
                    captureException = romanindexdict[withpreviousCHR]
                    capturePreviousCHR = romanindexdict[(s[counter-1])]
                    addromans = addromans + captureException - capturePreviousCHR
                else:
                    romanlookup = romanindexdict[i]
                    addromans = addromans + romanlookup 
        return addromans
        
        
test1 = Solution().romanToInt('MCMXCIV')
print(test1)
test2 = Solution().romanToInt('LVIII')
print(test2)
test3 = Solution().romanToInt('MMMCMXCIX')
print(test3)
