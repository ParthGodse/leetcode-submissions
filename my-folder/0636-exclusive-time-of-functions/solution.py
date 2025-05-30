class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        executiontimes = [0] * n

        stack = []
        prev_start = 0

        for log in logs:
            fid, call, timestamp = log.split(":")

            fid = int(fid)
            timestamp = int(timestamp)
            if call == "start":
                if stack:
                    executiontimes[stack[-1]] += timestamp - prev_start
                stack.append(fid)
                prev_start = timestamp
            else:
                executiontimes[stack.pop()] += timestamp - prev_start + 1
                prev_start = timestamp + 1 
        return executiontimes
