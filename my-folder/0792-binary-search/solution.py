class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        # l, h = 0, len(nums) - 1
        # while l<=h:
        #     m = (l + h) //2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         h = m - 1
        # return -1
        def binary(l, h):
            if l>h:
                return -1
            while l<=h:
                m = (l + h) //2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    return binary(m+1,h)
                else:
                    return binary(l,m-1)

        return binary(0,len(nums)-1)

