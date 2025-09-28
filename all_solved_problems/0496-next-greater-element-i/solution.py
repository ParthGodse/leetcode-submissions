class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        mapping = {}
        
        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)
            
        while stack:
            mapping[stack.pop()] = -1
            
        for num in nums1:
            res.append(mapping[num])

        return res

