class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(0, len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        l , r = 0, len(numbers) - 1
        while l<r:
            if numbers[l] + numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1        
