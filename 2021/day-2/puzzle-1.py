def puzzle_1():
    lines = read_lines('./puzzle-1.input')
    return calculate_position(lines)

def puzzle_2():
    lines = read_lines('./puzzle-1.input')
    return calculate_position_with_aim(lines)

def read_lines(path):
    with open(path) as f:
        return f.readlines()

def calculate_position(info):
    location = [0,0,0,0]
    backward = 0
    forward = 1
    up = 2
    down = 3

    update_position = lambda location, values, direction: location[direction] + int(values.split(' ')[1].strip())

    for coords in info:
        if coords.startswith("backward"):
            location[backward] = update_position(location, coords, backward)

        if coords.startswith("forward"):
            location[forward] = update_position(location, coords, forward)

        if coords.startswith("up"):
            location[up] = update_position(location, coords, up)

        if coords.startswith("down"):
            location[down] = update_position(location, coords, down)

    absolute_location = (location[forward] - location[backward]) * (location[down] - location[up])
    return absolute_location


def calculate_position_with_aim(info):
    dashboard = {
        'aim': 0,
        'depth': 0,
        'position': 0
    }

    for coords in info:
        instruction = coords.split(' ')[0].strip()
        units = int(coords.split(' ')[1].strip())

        if instruction == "forward":
            dashboard['position'] = dashboard['position'] + units
            dashboard['depth'] =  dashboard['depth'] + (units * dashboard['aim'])

        if instruction == 'down':
            dashboard['aim'] = dashboard['aim'] + units

        if instruction == 'up':
            dashboard['aim'] = dashboard['aim'] - units

    return dashboard['position'] * dashboard['depth']

print(f'Solution is {puzzle_2()}')
