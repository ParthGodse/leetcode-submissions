class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        q = deque([0])
        seen.add(0)

        while q:
            room = q.popleft()
            for key in rooms[room]:
                if key not in seen:
                    seen.add(key)
                    q.append(key)

        return len(seen) == len(rooms)

