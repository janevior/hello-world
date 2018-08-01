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
