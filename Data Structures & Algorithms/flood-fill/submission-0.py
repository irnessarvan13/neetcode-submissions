class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        originalColor = image[sr][sc]
        if originalColor == color:
            return image
        
        def dfs(image, r, c):
            rows = len(image)
            cols = len(image[0])
            
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if image[r][c] != originalColor:
                return
            
            image[r][c] = color
            
            dfs(image, r + 1, c)
            dfs(image, r - 1, c)
            dfs(image, r, c + 1)
            dfs(image, r, c - 1)
        
        dfs(image, sr, sc)
        return image