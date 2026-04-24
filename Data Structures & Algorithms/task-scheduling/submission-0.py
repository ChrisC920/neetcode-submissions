class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)

        res = 0
        q = deque()
        while heap or q:
            res += 1

            if not heap:
                res = q[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                print(cnt)
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush(heap, q.popleft()[0])
        
        return res