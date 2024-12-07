class Solution:
    def checkValidString(self, s: str) -> bool:

        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

        """
        If the `leftmin` becomes negative, 
        it indicates that we've encountered more right parentheses 
        than the total number of corresponding left parentheses and asterisks seen so far. 
        In such cases, we can revise the previous characters to include an empty space, 
        utilizing the wildcard '*' as an optional left parenthesis. 
        This gives the string another chance to remain valid. 

        About that part where we reset leftMin to 0 if it's negative. 
        Take for example a string that looks like this  
        "(((***". After we have parsed this string our leftMax wil be 6 
        and our leftMin will be 0 which should return true 
        because we can change every asterisk symbol for a right parenthesis symbol. 
        But if we add another asterisk to that string 
        "(((****" our leftMin will become -1. 
        But in this case it doesn't make any sense for us to turn every asterisk into 
        a right parenthesis because it will make the whole string invalid, 
        that's why we treat one asterisk as an empty string and reset our leftMin to 0. 
        And we don't afraid of a case like this "())" 
        where we also should reset our leftMin because our leftMax will 
        become less than 0 and it will return false.
        """