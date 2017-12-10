from functools import reduce
from operator import xor

def splice(lst1, lst2, index):
    spliced = list(lst1)
    for i, val in enumerate(lst2):
        splice_idx = (index+i) % len(spliced)
        spliced[splice_idx] = val
    return spliced


def sublist(lst, start, length):
    sub = []
    for i in range(start, start+length):
        idx = i % len(lst)
        sub.append(lst[idx])
    return sub


def reverse(lst, start, length):
    sub = sublist(lst, start, length)
    sub.reverse()
    return splice(lst, sub, start)


def solve(size, inputs):
    string = list(range(size))
    skip = 0
    pos = 0
    for length in inputs:
        string = reverse(string, pos, length)
        pos = (pos + skip + length) % len(string)
        skip += 1
    return string


def sparse_to_dense(inputs):
    result = []
    for i in range(16):
        block = inputs[i*16:i*16+16]
        result.append(reduce(xor, block))
    return "".join("%02x" % b for b in result)


def elf_hash(string):
    state = list(range(256))
    inputs = [ord(str(c)) for c in string]
    inputs.extend([17, 31, 73, 47, 23])
    skip = 0
    pos = 0
    for _round in range(64):
        for length in inputs:
            state = reverse(state, pos, length)
            pos = (pos + skip + length) % len(state)
            skip += 1
    return sparse_to_dense(state)


sample = [3, 4, 1, 5]
sample_solution = solve(5, sample)
assert sample_solution == [3, 4, 2, 1, 0]
print("Sample tested ok")


with open('10-input.txt') as f:
    lengths = f.read().strip()
hashed = solve(256, [int(c) for c in lengths.split(',')])
print("Solution 1:", hashed[0] * hashed[1])


tcs = [
    ('','a2582a3a0e66e6e86e3812dcb672a272'),
    ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
    ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
    ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')
]
for indata, expected in tcs:
    actual = elf_hash(indata)
    assert actual == expected, "%s != %s" % (actual, expected)
print('All test cases passed')

solution2 = elf_hash(lengths)
print("Solution 2:", solution2)
