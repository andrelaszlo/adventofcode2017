from collections import namedtuple


class ParseError(Exception):
    def __init__(self, index, msg):
        super().__init__()
        self.index = index
        self.msg = msg

    def __str__(self):
        return "%d: %s" % (self.index, self.msg)


Group = namedtuple('Group', ['children'])
Garbage = namedtuple('Garbage', ['content'])


# States
S_INITIAL = 'initial'
S_GROUP = 'group'
S_GARBAGE = 'garbage'
S_ESCAPE = 'escape'


def parse(indata):
    state = S_INITIAL
    group_stack = []
    state_stack = []
    try:
        for index, c in enumerate(indata):
            if state is S_INITIAL:
                if c == '{':
                    group_stack.append(Group(children=[]))
                    state_stack.append(state)
                    state = S_GROUP
                else: raise ParseError(index, 'Stream does not start with a group')
            elif state is S_GROUP:
                if c == '{':
                    group_stack.append(Group(children=[]))
                    state_stack.append(state)
                    state = S_GROUP
                elif c == '}':
                    current_group = group_stack.pop()
                    state = state_stack.pop()
                    if state == S_INITIAL:
                        return current_group
                    else:
                        group_stack[-1].children.append(current_group)
                elif c == '<':
                    group_stack[-1].children.append(Garbage(content=[]))
                    state_stack.append(state)
                    state = S_GARBAGE
                elif c == ',':
                    pass
                else:
                    raise ParseError(index, '%s is not defined in a group' % c)
            elif state is S_GARBAGE:
                if c == '!':
                    state = S_ESCAPE
                elif c == '>':
                    state = state_stack.pop()
                else:
                    garbage = group_stack[-1].children[-1]
                    garbage.content.append(c)
            elif state is S_ESCAPE:
                state = S_GARBAGE
            else:
                raise ParseError(index, 'Unknown state %s' % state)

        raise ParseError(index, 'Unclosed groups at end of stream')
    except ParseError as pe:
        print(pe)


def score(node, current=0):
    if isinstance(node, Group):
        return current+1 + sum(score(child, current+1) for child in node.children)
    return 0


def score_garbage(node):
    if isinstance(node, Group):
        return sum(score_garbage(child) for child in node.children)
    return len(node.content)


tests = [
    ('{}', 1),
    ('{{{}}}', 6),
    ('{{},{}}', 5),
    ('{{{},{},{{}}}}', 16),
    ('{<a>,<a>,<a>,<a>}', 1),
    ('{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
    ('{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
    ('{{<a!>},{<a!>},{<a!>},{<ab>}}', 3)
]
for stream, expected in tests:
    assert score(parse(stream)) == expected
print('All tests ok')

with open('9-input.txt') as f:
    stream = f.read()
print("Solution 1:", score(parse(stream)))
print("Solution 2:", score_garbage(parse(stream)))
