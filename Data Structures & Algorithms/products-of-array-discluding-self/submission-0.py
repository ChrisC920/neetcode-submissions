class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        isZero = False
        for n in nums:
            if n != 0:
                prod *= n
            else:
                isZero = True
        
        res = []
        for n in nums:
            if isZero:
                res.append(0 if (n != 0) else prod)
            else:
                res.append(int(prod / n) if (n != 0) else prod)
        return res