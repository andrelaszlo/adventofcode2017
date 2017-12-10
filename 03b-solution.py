from collections import defaultdict

class Grid():
    def __init__(self):
        self._grid = defaultdict(lambda: None)
        self._bounds = (0, 0, 0, 0) # min x, max x, min y, max y
        self._minx = 0
        self._maxx = 0
        self._miny = 0
        self._maxy = 0
        self._valsize = 1

    def get(self, x, y):
        return self._grid[(x, y)] if (x, y) in self._grid else None

    def set(self, x, y, val):
        self._update_bounds(x, y)
        self._valsize = max(self._valsize, len(str(val)))
        self._grid[(x, y)] = val

    def _update_bounds(self, x, y):
        self._minx = min(x, self._minx)
        self._maxx = max(x, self._maxx)
        self._miny = min(y, self._miny)
        self._maxy = max(y, self._maxy)

    def print(self):
        spacer = " "
        fmt = "{:%s>%d}" % (spacer, self._valsize)
        for y in range(self._miny, self._maxy + 1):
            for x in range(self._minx, self._maxx + 1):
                value = self.get(x, y)
                item = fmt.format(value) if value else "..."
                print(item, end=spacer)
            print()

L = (-1, 0)
R = (1, 0)
U = (0, -1)
D = (0, 1)

def spiral_stepper(g):
    yield (0, 0)
    x, y = (1, 0)
    direction_counter = 0
    directions = [U, L, D, R]
    dx, dy = directions[0]
    while True:
        yield (x, y)
        check_x, check_y = directions[(direction_counter+1) % len(directions)]

        if not g.get(x + check_x, y + check_y):
            direction_counter += 1 # change direction

        # move a step in this direction
        dx, dy = directions[direction_counter % len(directions)]
        x += dx
        y += dy

def filled_grid(size):
    g = Grid()
    n = 1
    for x, y in spiral_stepper(g):
        g.set(x, y, n)
        if n == size: break
        n += 1
    return x, y, g

def neighbor_sum(g, x, y):
    return sum((
        g.get(x-1, y-1) or 0,
        g.get(x  , y-1) or 0,
        g.get(x+1, y-1) or 0,
        g.get(x-1, y  ) or 0,
        g.get(x+1, y  ) or 0,
        g.get(x-1, y+1) or 0,
        g.get(x  , y+1) or 0,
        g.get(x+1, y+1) or 0,
    ))

x, y, g = filled_grid(368078)
solution_1 = abs(x) + abs(y)
print("Solution 1:", solution_1)

def accumulating_grid(n):
    g = Grid()
    for x, y in spiral_stepper(g):
        if x == y == 0:
            g.set(x, y, 1)
        else:
            val = neighbor_sum(g, x, y)
            g.set(x, y, val)
            if val > n:
                return val

print("Solution 2:", accumulating_grid(368078))
