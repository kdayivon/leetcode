class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n:int = len(blocks)
        w_count = blocks[:k].count("W")
        min_win = w_count
        for i in range(k, n):
            if (blocks[i - k] == "W"):
                w_count -= 1
            if (blocks[i] == "W"):
                w_count += 1
            min_win = min(min_win, w_count)
        return min_win

