class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        validLetters = "abcdefghijklmnopqrstuvwxyz0123456789"
        l, r = 0, len(lower) - 1
        while l < r:
            while l < r and lower[l] not in validLetters:
                l += 1
            while l < r and lower[r] not in validLetters:
                r -= 1
            print(f"{l} {r}")
            if lower[l] != lower[r]:
                return False
            l += 1
            r -= 1
        return True