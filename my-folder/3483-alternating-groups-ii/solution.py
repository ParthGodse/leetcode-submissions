class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # n = len(colors)

        # start_index = 0
        # for i in range(n):
        #     if colors[i] == colors[(i - 1) % n]:
        #         start_index = i

        # count = 0
        # for i in range(n):  # Try each position as a possible start
        #     valid = True
        #     for j in range(k - 1):
        #         if colors[(i + j) % n] == colors[(i + j + 1) % n]:  # Check if not alternating
        #             valid = False
        #             break
        #     if valid:
        #         count += 1
        # return count
        n = len(colors) 
        count = 0
        left = 0

        for right in range(n + k - 1):
            if right > 0 and colors[right % n] == colors[(right - 1) % n]:
                left = right  
            
            if right - left + 1 >= k:
                count += 1  
        
        return count
