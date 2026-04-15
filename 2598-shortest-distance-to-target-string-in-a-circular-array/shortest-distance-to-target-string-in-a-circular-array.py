class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        
        n = len(words)
        mini = float('inf')
        
        for i in range(n):
            if words[i] == target:
                # clockwise distance
                right = (i - startIndex + n) % n
                # anticlockwise distance
                left = (startIndex - i + n) % n
                
                mini = min(mini, right, left)
        
        return mini