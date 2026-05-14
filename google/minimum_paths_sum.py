from typing import List, Optional

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0:
            return 0

        def min_prev_positions(pos: tuple[int,int]) -> int:
            up, left = (pos[0]-1,pos[1]), (pos[0],pos[1]-1)
            upv = leftv = sentinel

            if up[0]>=0:
                upv = grid[up[0]][up[1]]

            if left[1]>=0:
                leftv = grid[left[0]][left[1]]

            return min(upv, leftv)

        sentinel = float('inf')
        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                min_prev = min_prev_positions((x,y))
                min_prev = 0 if min_prev == sentinel else min_prev
                grid[x][y] += min_prev

        return grid[-1][-1]

"""
    Alg analysis:
         !(n-1)
"""

if __name__ == '__main__':
    s = Solution()

    assert s.minPathSum(grid=[[1,3,1],[1,5,1],[4,2,1]]) == 7
