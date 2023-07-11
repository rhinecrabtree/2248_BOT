grid = ([
    [  8,  32,  64,   2,  32],
    [ 32,  64,  64,   4,   8],
    [  2,   4,  64,   4,   2],
    [  4,   8, 128,  16,  64],
    [ 16,  32,   2,  32,   8],
    [ 32,   8,   8,   2,   4],
    [128,  32,   4, 128,   8],
    [  4,   8,  64,   2,  32]])

def find_longest_chain(grid):
    def dfs(row, col, chain, first_move_made):
        # Check if the current position is a valid next move in the chain
        if (not first_move_made and grid[row][col] == chain[-1]) or (first_move_made and grid[row][col] == chain[-1]*2):
            # Add the current position to the chain
            chain.append(grid[row][col])
            # Recursively search for the next move in all adjacent positions
            longest_chain = chain
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] not in chain:
                    new_chain = dfs(r, c, chain[:], True)
                    if len(new_chain) > len(longest_chain):
                        longest_chain = new_chain
            return longest_chain
        else:
            # If the current position is not a valid next move, return the current chain
            return chain
    
    # Search for the longest chain starting from each position with a value of 2
    longest_chain = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 2:
                chain = dfs(row, col, [2], False)
                if len(chain) > len(longest_chain):
                    longest_chain = chain
                    
    return longest_chain

print(find_longest_chain(grid))