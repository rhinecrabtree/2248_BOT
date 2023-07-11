import numpy as np

game_board = np.array([[8, 32, 64, 2, 32],
                       [32, 64, 64, 4, 8],
                       [2, 4, 64, 4, 2],
                       [4, 8, 128, 16, 64],
                       [16, 32, 2, 32, 8],
                       [32, 8, 8, 2, 4],
                       [128, 32, 4, 128, 8],
                       [4, 8, 64, 2, 32]])

class Solver:
    def __init__(self, game_board):
        self.game_board = game_board

    def find_first_moves(self):
        first_moves = []
        for row in range(self.game_board.shape[0]):
            for col in range(self.game_board.shape[1]):
                adj_tiles = self.get_adjacent_tiles((row, col))
                for tile in adj_tiles:
                    if tile[1] == self.game_board[row, col]:
                        first_moves.append(((row, col), tile[0]))
        if len(first_moves) == 0:
            return None
        else:
            return first_moves

    def get_adjacent_tiles(self, tile):
        adj_tiles = []
        row = tile[0]
        col = tile[1]
        if row != 0:
            adj_tiles.append(((row - 1), col, self.game_board[row - 1, col]))
        if row != self.game_board.shape[0] - 1:
            adj_tiles.append(((row + 1), col, self.game_board[row + 1, col]))
        if col != 0:
            adj_tiles.append((row, (col - 1), self.game_board[row, col - 1]))
        if col != self.game_board.shape[1] - 1:
            adj_tiles.append((row, (col + 1), self.game_board[row, col + 1]))
        return adj_tiles
    def get_adjacent_tiles(self, pos):

        # Create a list to store the adjacent tiles
        adj_tiles = []

        # Create a list to store the directions of the adjacent and diagonal tiles.
        directions = [  
            (0, 1),     # Right
            (1, 1),     # Down Right
            (1, 0),     # Down
            (1, -1),    # Down Left
            (0, -1),    # Left
            (-1, -1),   # Up Left
            (-1, 0),    # Up
            (-1, 1)    # Up Right
            ]

        # Iterate through the directions list to find the adjacent tiles
        for row_dir, col_dir in directions:
            # Create a variable to store the row and column of the adjacent tile
            row, col = pos[0] + row_dir, pos[1] + col_dir
            # Check if the adjacent tile is within the bounds of the game board
            if 0 <= row < self.game_board.shape[0] and 0 <= col < self.game_board.shape[1]:
                # Add the adjacent tile to the adj_tiles list
                adj_tiles.append(((row, col), self.game_board[row, col]))

        # Return the adj_tiles list
        return adj_tiles

    # Function to check the adjacent tiles for a valid move and return the position of the tile to move to. If no valid move is found, return None.
    def check_adjacent_tiles(self, pos):
        # Compare the value of the current position to the value of each adjacent and diagonal tile. If the value of the current position is equal to any of the adjacent or diagonal tiles or if any of the adjacent or diagonal tiles are equal to the value of the current position multiplied by 2, then the move is valid and the function should return that tile's position. If none of the adjacent or diagonal tiles are equal to the value of the current position or the value of the current position multiplied by 2, then the move is invalid and the function should return None.
        pass