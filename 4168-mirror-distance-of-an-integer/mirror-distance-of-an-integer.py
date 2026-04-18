class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(x):
            return int(x[::-1])
        return abs(n-reverse(str(n)))
        