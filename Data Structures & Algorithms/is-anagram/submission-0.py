class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charsS = {}
        for char in s:
            if char in charsS:
                charsS[char] = charsS[char] + 1
            else:
                charsS[char] = 1
        charsT = {}
        for char in t:
            if char in charsT:
                charsT[char] = charsT[char] + 1
            else:
                charsT[char] = 1
        return charsT == charsS
                