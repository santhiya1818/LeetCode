class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
    
        length = (1 << n) - 1
        mid = (length // 2) + 1
    
    # Middle element
        if k == mid:
            return "1"
    
    # Left half
        if k < mid:
            return self.findKthBit(n - 1, k)
    
    # Right half
        mirrored = length - k + 1
        bit = self.findKthBit(n - 1, mirrored)
    
    # Invert the bit
        return "1" if bit == "0" else "0"