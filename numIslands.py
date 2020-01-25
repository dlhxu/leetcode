class Solution(object):
    # recursive helper
    def checkNeighbors(self, row, column, grid):
        # recurse when a one has been found
        if (grid[row][column] == '1'):
            grid[row][column] = '0'
            # recurse on NSEW neighbors
            # check north
            if(row > 0): self.checkNeighbors(row - 1,column,grid)
            # check south
            if(row < maxRows - 1): self.checkNeighbors(row + 1,column,grid)
            # check west
            if(column > 0): self.checkNeighbors(row,column - 1,grid)
            # check east
            if(column < maxColumns - 1): self.checkNeighbors(row,column + 1,grid)
                
        # else recursive calls end
        
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        numIslands = 0
        
        global maxColumns
        global maxRows
        
        # check for empty grid
        if not grid:
            return numIslands
        
        maxColumns = len(grid[0])
        maxRows = len(grid)
        
        # traverse the entire grid
        for row in range(maxRows):
            for column in range(maxColumns):
                print(grid[row][column])
                # if an island is found
                if (grid[row][column] == '1'):
                    # increment number of islands and change value to 0 to prevent rechecking
                    numIslands +=1
                    
                    # perform DFS on all NSEW neighbors
                    self.checkNeighbors(row,column,grid)
                  
               # any subsequent iterations will now ONLY find disconnected ones, i.e. islands        
        return numIslands

