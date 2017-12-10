import re

def parse_pos(pos):
    pos_type = 'position' if pos[0] == '[' else 'move'
    location = [int(n) for n in pos.strip("()[]").split(',')]
    return (pos_type, location)


with open('00-infi-input.txt') as f:
    indata = f.read()

positions = [parse_pos(pos) for pos in re.findall(r'[([].*?[)\]]', indata)]
robot_positions = []
current = 0
collisions = 0

for pos_type, location in positions:
    if pos_type == 'position':
        robot_positions.append(location)
    else:
        current_loc = robot_positions[current]
        xd, yd = location
        current_loc[0] += xd
        current_loc[1] += yd
        for idx, pos in enumerate(robot_positions):
            if idx == current:
                continue
            if pos == current_loc:
                x, y = pos
                print(x, y)  # The collisions are pixels in an image =)
                collisions += 1
        current = (current+1) % len(robot_positions)

print("Total collisions", collisions)
