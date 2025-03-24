class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_r = deque()
        queue_d = deque()
        n = len(senate)

        for i , s in enumerate(senate):
            if s == 'R':
                queue_r.append(i)
            else:
                queue_d.append(i)

        while queue_r and queue_d:
            r_ind = queue_r.popleft()
            d_ind = queue_d.popleft()

            if r_ind < d_ind:
                queue_r.append(r_ind + n)
            else:
                queue_d.append(d_ind + n)

        if queue_r:
            return "Radiant"
        else:
            return "Dire"
