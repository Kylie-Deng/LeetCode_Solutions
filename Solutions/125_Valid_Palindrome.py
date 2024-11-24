class Solution:
    def isPalindrome(self, s: str) -> bool:

        if not s:
            return True

        i = 0
        j = len(s) - 1

        while i < j:

            while i < j and not (s[i].isalpha() or s[i].isdigit()):
                i += 1
            while i < j and not (s[j].isalpha() or s[j].isdigit()):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True