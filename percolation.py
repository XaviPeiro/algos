

class Percolation:
    grid: list[list[tuple[int, int] | None]]
    _percolates: bool
    _number_of_open_sites: int

    @staticmethod
    def _create_grid(width: int, height: int) -> list[list[tuple[int] | None]]:
        # grid = [[-1]*width]*height
        grid = []
        for y in range(height):
            grid.append([])
            for x in range(width):
                grid[y].append(None)
        return grid

    def _get_root(self, width: int, height: int) -> tuple | None:
        # TODO: Remember it can be None
        parent = self.grid[height][width]
        node = (height, width) if parent is not None else parent

        while parent != node:
            parent, node = self.grid[parent[0]][parent[1]], parent

        return node

    # Public API
    def __init__(self, grid_x_len: int, grid_y_len: int):
        self.grid = self._create_grid(width=grid_x_len, height=grid_y_len)
        self._percolates = False
        self._number_of_open_sites = 0

    def open(self, height: int, width: int):
        if self.grid[height][width] is None:
            self.grid[height][width] = (height, width)
            self._number_of_open_sites += 1
            # Check if there are open neighbours
            # weighted Quick Unions
            # Update _percolates if root row == 0

    def is_open(self, height: int, width: int) -> bool:
        return not (self.grid[height][width] is None)

    def is_full(self, height: int, width: int) -> bool:
        return self.is_open(height=height, width=width) and self._get_root(height, width)[0] == 0

    def number_of_open_sites(self) -> int:
        return self._number_of_open_sites

    def percolates(self) -> bool:
        return self._percolates







if __name__ == '__main__':
    # Tests

    # Grid creation
    grid_3_3 = Percolation._create_grid(3, 3)
    assert len(grid_3_3) == 3
    assert len(grid_3_3[0]) == 3
    assert grid_3_3[0][1] is None

    grid_4_10 = Percolation._create_grid(4, 10)
    assert len(grid_4_10) == 10
    assert len(grid_4_10[0]) == 4
    assert len(grid_4_10[3]) == 4
    assert grid_4_10[3][5] is None



