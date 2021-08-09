class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if word[0] == board[i][j] and self.dfs(self, board, i, j, 0, word):
                    return True
        return False

    def dfs(self, board: list[list[str]], i: int, j: int, count: int, word: str) -> bool:
        if(count == len(word)):
            return True
        if (i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[count]):
            return False
        tmp = board[i][j]
        board[i][j] = ' '
        found = self.dfs(self, board, i+1, j, count+1, word,) or self.dfs(self, board, i-1, j, count+1,
                                                                          word) or self.dfs(self, board, i, j+1, count+1, word) or self.dfs(self, board, i, j-1, count+1, word)
        board[i][j] = tmp
        return found


matrix = [
    ['F', 'A', 'C', 'I'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['M', 'A', 'S', 'S']]
s = Solution
print(s.exist(s, matrix, 'FOAM'))
