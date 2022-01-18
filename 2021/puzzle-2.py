def puzzle_1():
    lines = read_lines('./puzzle-1.test')
    return calculate_position(lines)

def read_lines(path):
    with open(path) as f:
        return f.readlines()

def calculate_position(lines):
    location = [0,0,0,0]
    backward = 0
    forward = 1
    up = 2
    down = 3

    update_position = lambda location, values, direction: location[direction] + int(values.strip(' ')[1].strip())

    for coords in info:
        if info.startswith("backward"):
            location[backward] = update_position(location, coords, backward)

        if info.startswith("forward"):
            location[forward] = update_position(location, coords, forward)

        if info.startswith("up"):
            location[up] = update_position(location, coords, up)

        if info.startswith("down"):
            location[down] = update_position(location, coords, down)

    absolute_location = (location[forward] - location[backward]) * (location[down] - location[up])
    return absolute_location


print(f'Solution is {puzzle_1()}')
