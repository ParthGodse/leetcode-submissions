class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        result = [True if (candy + extraCandies) >= max_value else False for candy in candies]
        return result
