class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for r in board:
            nums = [x for x in r if x != "."]
            if len(nums) > len(set(nums)):
                return False
        
        # Check cols

        def get_columns(board):
            for col in range(9):
                yield [board[row][col] for row in range(9)]

        for i, column in enumerate(get_columns(board)):
            nums = [x for x in column if x != "."]
            if len(nums) > len(set(nums)):
                return False
        

        def get_boxes(board):
            for box_row in range(3):
                for box_col in range(3):
                    box = []
                    for r in range(3):
                        for c in range(3):
                            box.append(board[box_row * 3 + r][box_col * 3 + c])
                    yield box
        

        for i, box in enumerate(get_boxes(board)):
            nums = [x for x in box if x != "."]
            if len(nums) > len(set(nums)):
                return False
        return True
            