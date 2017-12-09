import re
from collections import Counter

def parse_line(line):
    line = line.strip()
    program, weight, _, children = re.match("""(\w+) \((\d+)\)( -> (.*))?""", line).groups()
    weight = int(weight)
    children = children.split(', ') if children else []
    return program, weight, children
    

def build_tree(indata):
    positions = {program: {'program': program, 'weight': weight, 'children': children}
                 for program, weight, children in indata}
    possible_roots = set(program for program, item in positions.items() if item['children'])
    for root_candidate_key in list(possible_roots):
        root_candidate = positions[root_candidate_key]
        for child in root_candidate['children']:
            if child in possible_roots:
                possible_roots.remove(child)
    root = positions[possible_roots.pop()]
    stack = [root]
    while stack:
        current = stack.pop()
        children = current['children']
        for child in list(children):
            child_item = positions[child]
            children[children.index(child)] = child_item
            stack.append(child_item)
            
    return root


def print_tree(node, prefix=""):
    children = node['children']
    print("%s%s (%d)" % (prefix, node['program'], node['weight']), end=":\n" if children else "\n")
    for child in children:
        print_tree(child, prefix+"  ")


def check_weights(tree):
    _, errors = _check_weights(tree)
    return errors[0]

def _check_weights(tree, errors=None):
    if errors is None:
        errors = []
    if not tree['children']:
        return tree['weight'], errors
    child_weights = []
    for child in tree['children']:
        child_weight, _ = _check_weights(child, errors)
        child_weights.append((child, child_weight))
    weight_counts = Counter(weight for _, weight in child_weights)
    if len(weight_counts) > 1:
        good, bad = [k for k,v in weight_counts.most_common()]
        diff = good - bad
        for child, weight in child_weights:
            if weight == bad:
                correct = child['weight'] + diff
                errors.append("%s has total weight %d, should be %d. Own weight is %d, should be %d" %
                      (child['program'], weight, good, child['weight'], correct))
    return tree['weight'] + sum(weight for _, weight in child_weights), errors


sample = [parse_line(line) for line in """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".splitlines()
          if line]

tree = build_tree(sample)
#print_tree(tree)
print("Sample solution 1:", tree['program'])
print("Sample solution 2:", check_weights(tree))

with open('7-input.txt') as f:
    data = [parse_line(line.strip()) for line in f.readlines()]

tree = build_tree(data)
print("Solution 1:", tree['program'])
print("Solution 2:", check_weights(tree))

