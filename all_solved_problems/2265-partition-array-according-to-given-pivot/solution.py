class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        smaller = []
        res = [0] * len(nums)
        index, count = 0, 0

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            elif num == pivot:
                count += 1
        
        for i in smaller:
            res[index] = i
            index += 1
        
        for _ in range(count):
            res[index] = pivot
            index += 1

        for j in greater:
            res[index] = j
            index += 1

        return res        
