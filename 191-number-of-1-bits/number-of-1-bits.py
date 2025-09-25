class Solution:
    def hammingWeight(self, n: int) -> int:
        a=bin(n)[2:]
        return int(a.count('1'))