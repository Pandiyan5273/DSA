class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        nums=[str(i) for i in nums]
        def map_value(num):
            return int("".join(str(mapping[int(digit)]) for digit in num))
        mapping=[(num,map_value(num)) for num in nums]
        mapping.sort(key =lambda x:x[1])
        ans=[int(num) for num,i in mapping]
        return ans