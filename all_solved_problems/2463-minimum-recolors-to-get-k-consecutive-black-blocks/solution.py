class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        black = 0
        res = float('inf')
        for i in range(len(blocks)):
            if i - k >= 0 and blocks[i - k] == 'B':
                black -= 1
            if blocks[i] == 'B':
                black += 1
            res = min(res, k - black)

        return res 
