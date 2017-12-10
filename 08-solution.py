from collections import namedtuple, defaultdict

Operation = namedtuple('Operation', ['register', 'operator', 'parameter'])
Instruction = namedtuple('Instruction', ['operation', 'condition'])


OPERATORS = {
    '>': lambda register, argument, state: state[register] > argument,
    '<': lambda register, argument, state: state[register] < argument,
    '==': lambda register, argument, state: state[register] == argument,
    '>=': lambda register, argument, state: state[register] >= argument,
    '<=': lambda register, argument, state: state[register] <= argument,
    '!=': lambda register, argument, state: state[register] != argument,
    'inc': lambda register, argument, state: state.__setitem__(register, state[register] + argument),
    'dec': lambda register, argument, state: state.__setitem__(register, state[register] - argument),
}


def parse(program):
    return [parse_line(l) for l in program if l]


def parse_line(line):
    reg, op, param, _, cond_reg, cond_op, cond_param = line.split(" ")
    operation = Operation(reg, op, int(param))
    condition = Operation(cond_reg, cond_op, int(cond_param))
    return Instruction(operation, condition)


def evaluate(operation, state):
    return OPERATORS[operation.operator](operation.register, operation.parameter, state)


def run(program):
    state = defaultdict(int)
    maxval = 0
    for instruction in program:
        cond_result = evaluate(instruction.condition, state)
        if cond_result:
            evaluate(instruction.operation, state)
            maxval = max(maxval, max(state.values()))
    return state, maxval


sample_program = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""

final_state, maxval = run(parse(sample_program.splitlines()))
print("Sample result:", max(final_state.values()))
print("Sample max val:", maxval)

with open('8-input.txt') as f:
    final_state, maxval = run(parse(f.readlines()))
print("Solution 1:", max(final_state.values()))
print("Solution 2:", maxval)
