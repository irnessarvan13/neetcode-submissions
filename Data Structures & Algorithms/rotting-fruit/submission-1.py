from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        length = 0

        # Find all rotten and fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        while queue and fresh > 0:
            for _ in range(len(queue)):     # everything in the CURRENT ring
                r, c = queue.popleft()

                for dr, dc in [[1,0], [0,1], [-1,0], [0,-1]]:
                    newR = r + dr
                    newC = c + dc

                    if 0 <= newR < rows and 0 <= newC < cols:
                        if grid[newR][newC] == 1:
                            grid[newR][newC] = 2
                            fresh -= 1
                            queue.append((newR, newC))

            length += 1                    # one full ring = one minute

        if fresh == 0:
            return length
        else:
            return -1