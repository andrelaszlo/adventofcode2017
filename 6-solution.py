def redist_index(state):
    maximum = max(state)
    return state.index(maximum)


def solve(indata):
    state = list(indata)
    solution = 0
    seen = set()
    seen.add(tuple(indata))

    while True:
        index = redist_index(state)
        value = state[index]
        state[index] = 0
        while value > 0:
            index = (index + 1) % len(state) # cache len?
            state[index] += 1
            value -= 1
        fingerprint = tuple(state)
        solution += 1
        if fingerprint in seen:
            return solution, state
        seen.add(fingerprint)


sample = [0, 2, 7, 0]
print("Sample solution", solve(sample))

with open('6-input.txt') as f:
    data = f.read()
indata = [int(c) for c in data.strip().split('\t')]
solution, state = solve(indata)
print("Solution 1:", solution)

solution, state = solve(state)
print("Solution 2:", solution)
