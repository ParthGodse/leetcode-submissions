class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n = len(set(nums))
        nums.sort()
        for i in range(3):
            if nums[0] + nums[1] > nums[2]:
                if n == 1:
                    return "equilateral"
                elif n == 2:
                    return "isosceles"
                else:
                    return "scalene"
            else:
                return "none"
