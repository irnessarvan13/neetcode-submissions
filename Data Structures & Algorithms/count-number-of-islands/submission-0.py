class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(grid, r, c, visited):
            rows = len(grid)
            cols = len(grid[0])

            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            
            if grid[r][c] == '0':
                return

            if (r, c) in visited:
                return
            
            visited.add((r, c))

            dfs(grid, r + 1, c, visited)
            dfs(grid, r - 1, c, visited)
            dfs(grid, r, c + 1, visited)
            dfs(grid, r, c - 1, visited)
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    count += 1
                    dfs(grid, r, c, visited)
        return count
        