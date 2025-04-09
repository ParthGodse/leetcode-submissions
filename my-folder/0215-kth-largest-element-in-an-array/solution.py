class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in nums:
            minheap.append(i)
        heapq.heapify(minheap)  
        while len(minheap) > k:
            heapq.heappop(minheap)
        return minheap[0]
        # heap = nums[:k]
        # heapq.heapify(heap)
        
        # for num in nums[k:]:
        #     if num > heap[0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, num)
        
        # return heap[0]
        #return heapq.nlargest(k, nums)[-1]
