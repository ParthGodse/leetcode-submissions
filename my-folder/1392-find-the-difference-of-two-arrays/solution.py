class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # res1 = []
        # res2 = []
        # for num in nums1:
        #     if num not in nums2 and num not in res1:
        #         res1.append(num)

        # for num in nums2:
        #     if num not in nums1 and num not in res2:
        #         res2.append(num)

        # return [res1, res2] 
        res1, res2 = set(nums1), set(nums2)
        return[list(res1 - res2), list(res2 - res1)]
