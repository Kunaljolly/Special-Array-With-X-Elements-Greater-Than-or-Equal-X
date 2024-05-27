
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            c = 0
            for y in nums:
                if y >= x:
                    c += 1
            if c == x:
                return x
        return -1
