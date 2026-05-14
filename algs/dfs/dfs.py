from typing import List


class DFS:
    def __call__(self, matrix: list[list[int]]):
        sums = []

        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[x])):
                ...

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


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> tuple[tuple[int,int], tuple[int,int]]:
        def go_all_next(pos: tuple[int,int]) -> int:
            d, r = (pos[0]+1,pos[1]), (pos[0],pos[1]+1)
            return (d,r)

        


