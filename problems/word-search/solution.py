class Solution:
    def exist(self, board, word: str) -> bool:
        """O(w * b) time | O(w) space | w->word, b->board"""
        if not word or not board: return False
        self.board = board
        self.word = word
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and self.search(row, col, 0, {}):
                    return True
        return False
    
    def search(s, row, col, idx, seen):
        if idx >= len(s.word): return True
        valid = (
            0 <= row < len(s.board) 
            and 0 <= col < len(s.board[0]) 
            and s.board[row][col] == s.word[idx]
            and seen.get((row, col), 0) == 0
        )
        if not valid: return False
        seen[(row, col)] = seen.get((row, col), 0) + 1
        result = False
        for r, c in [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]:
            result = result or s.search(r, c, idx+1, seen)
        seen[(row, col)] = seen.get((row, col), 0) - 1
        return result
