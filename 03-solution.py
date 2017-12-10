import unittest

# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.

# 37  36  35  34  33  32  31

# 38  17  16  15  14  13  30

# 39  18   5   4   3  12  29

# 40  19   6   1   2  11  28  <-- center

# 41  20   7   8   9  10  27

# 42  21  22  23  24  25  26

# 43  44  45  46  47  48  49 ->

def layers():
    n = 1
    layer = 0
    side = layer+1
    layer_size = 1
    yield layer, layer_size, n
    while True:
        layer += 1
        side = layer+1
        layer_size = 8*layer
        n += layer_size
        yield layer, layer_size, n

def solution(n):
    if n == 1:
        return 0
    for layer, layer_size, n_ in layers():
        if n_ >= n:
            break
    side = layer_size//4
    start = n_ - layer_size + 1
    offset = (n - start) % side
    center = side//2
    center_offset = max((offset+1) - center, center - (offset+1))
    #print("found", n, layer, layer_size, side, center_offset)
    return layer + center_offset


class TestSpiral(unittest.TestCase):
    def test_gen(self):
        l = layers()
        self.assertEqual(next(l), (0, 1, 1))
        self.assertEqual(next(l), (1, 8, 9))
        self.assertEqual(next(l), (2, 16, 25))
        self.assertEqual(next(l), (3, 24, 49))
    
    def test_1(self):
        self.assertEqual(solution(1), 0)

    def test_12(self):
        self.assertEqual(solution(12), 3)

    def test_23(self):
        self.assertEqual(solution(23), 2)

    def test_1024(self):
        self.assertEqual(solution(1024), 31)


if __name__ == '__main__':
    print("Solution:", solution(368078))
    unittest.main()
