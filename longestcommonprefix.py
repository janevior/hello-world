class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        
        noMatch = "N/A"
        fstlettercheck = ""
        
        for fststrcycle in strs:
            if fststrcycle == strs[0]:
                fstletter = fststrcycle[:1]
            else:
                fstlettercheck = fststrcycle[:1]
                if fstlettercheck == fstletter:
                    lastprefix = fstletter
                    continue            
                else:
                    return noMatch
                
        for secondlettercycle in strs:
            if secondlettercycle == strs[0]:
                secondletter = secondlettercycle[:2]
            else:
                secondlettercheck = secondlettercycle[:2]
                if secondlettercheck == secondletter:
                    continue            
                else:
                    return lastprefix
        
        lastprefix = secondletter
                    
        for thirdlettercycle in strs:
            if thirdlettercycle == strs[0]:
                thirdletter = thirdlettercycle[:3]
            else:
                thirdlettercheck = thirdlettercycle[:3]
                if thirdlettercheck == thirdletter:
                    continue            
                else:
                    return lastprefix
        
        lastprefix = thirdletter
                    
        for fourthlettercycle in strs:
            if fourthlettercycle == strs[0]:
                fourthletter = fourthlettercycle[:4]
            else:
                fourthlettercheck = fourthlettercycle[:4]
                if fourthlettercheck == fourthletter:
                    continue            
                else:
                    return lastprefix
        
        lastprefix = fourthletter
        
        return lastprefix

test1 = Solution().longestCommonPrefix(["flower","flow","flight"])
print(test1)

"""
OTHER SOLUTIONS: 

Here they have used range function to loop with integer - "length" of first string, 
then looping through the list from second string onwards, 
to see if the character in other string based on the iteration is same as the first string.
When the if returns false, then they capture the string to the length the iteration went on for. 

if not strs:
       return ""
for i in range(len(strs[0])):
       for string in strs[1:]:
             if i >= len(string) or string[i] != strs[0][i]:
                  return strs[0][:i]
       return strs[0]

Here they have used min method of string, but in this case on the list with option length. 
Then performed enmeration loop, through that string, while looping through other strings in the list
to check if the character on the other strings match first, when not found
return the number of character - iterations for the shortest string.

if not strs:
       return ""
shortest = min(strs,key=len)
for i, ch in enumerate(shortest):
       for other in strs:
             if other[i] != ch:
                  return shortest[:i]
       return shortest

"""
