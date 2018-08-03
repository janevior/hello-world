"""
Correct solution given by others:

Here you can see how they have used datatype "set" for open braces, followed by a set of tuples with both open and close braces. 
Then after creating an empty list, the solution iterates through the string, capture the open braces in an empty list,
just to be popped out, the next closed brace come to check for validity with tuple set. 


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
    
        s1=set('{[(')
        match=set([('(',')'),('{','}'),('[',']')])
        seen=[]

        for char in s:
            if char in s1:
                seen.append(char)
            else:
                if len(seen)==0:
                    return False
                lastOpen=seen.pop()
                if (lastOpen, char) not in match:
                    return False
        return len(seen)==0

test2 = Solution().isValid("(}")
test1 = Solution().isValid("(([]){})")


Below solution is my solution which is incorrect - for it fails the test
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        
        for i in s:
            if i == '(':
                a = ')'
                if a in s:
                    x = s[s.find(i)+1:s.find(a)]
                    if "" not in x:
                        continue
                    else:
                        if "(" in x:
                            if ")" not in x:
                                return False
                        if "{" in x:
                            if "}" not in x:
                                return False
                        if "[" in x:
                            if "]" not in x:
                                return False
                else:
                    return False
                    
            if i == '{':
                b = '}'
                if b in s:
                    x = s[s.find(i)+1:s.find(b)]
                    if "" not in x:
                        continue
                    else:
                        if "(" in x:
                            if ")" not in x:
                                return False
                        if "{" in x:
                            if "}" not in x:
                                return False
                        if "[" in x:
                            if "]" not in x:
                                return False
                else:
                    return False
                    
            if i == '[':
                c = ']'
                if c in s:
                    x = s[s.find(i)+1:s.find(c)]
                    if "" not in x:
                        continue
                    else:
                        if "(" in x:
                            if ")" not in x:
                                return False
                        if "{" in x:
                            if "}" not in x:
                                return False
                        if "[" in x:
                            if "]" not in x:
                                return False
                else:
                    return False
            if i == ')':
                a = '('
                if a not in s:
                    return False
            if i == '}':
                a = '{'
                if a not in s:
                    return False
            if i == ']':
                a = '['
                if a not in s:
                    return False
                    
        return True

test1 = Solution().isValid("(([]){})")
