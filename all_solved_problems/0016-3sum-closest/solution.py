class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # res = []
        # for i in range(n - 2):
        #     for j in range(i + 1, n - 1):
        #         for k in range(j + 1, n):
        #             three = nums[i] + nums[j] + nums[k]
        #             res.append(three)

        # min_diff = float('inf')
        # best_three = None
        # for idx, three in enumerate(res):
        #     diff = abs(target - three)
        #     if diff < min_diff:
        #         min_diff = diff
        #         best_three = three

        # return best_three
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                curr = nums[i] + nums [l] + nums[r]

                if abs(target - curr) < abs(target - closest):
                    closest = curr

                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    return target

        return closest 
