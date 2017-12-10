sample = [0, 3, 0, 1, -3]

def run(offsets, rule2=False):
    offsets = list(offsets)
    n = 0
    pc = 0
    while True:
        #print(offsets, pc)
        inc = offsets[pc]
        nxt = pc + inc
        if rule2:
            if offsets[pc] >= 3:
                offsets[pc] -= 1
            else:
                offsets[pc] += 1
        else:
            offsets[pc] += 1
        pc = nxt
        n += 1
        if pc >= len(offsets) or pc < 0:
            #print(offsets, pc, "DONE")
            return n


print("Sample output:", run(sample))

with open('5-input.txt') as f:
    data = f.readlines()
data = [int(c.strip()) for c in data]

print("Solution 1:", run(data))
print("Sample output 2:", run(sample, True))
print("Solution 2:", run(data, True))
