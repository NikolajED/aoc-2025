
def get_number_from_line(line):
    if line.startswith('R'):
        line = line.replace("R", "")
        return int(line)
    elif line.startswith('L'):
        line = line.replace("L", "")
        return int(line)
    return 0

def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

start_position = 50
min_position = 0
max_position = 99
times_hit_min = 0
lines = read_lines_from_file('puzzle_input.txt')

current_position = start_position
for line in lines:
    move_by = get_number_from_line(line)
    print(f"Moving {line} by {move_by} from {current_position}")
    for _ in range(move_by):
        if line.startswith('R'):
            current_position += 1
            if current_position > max_position:
                current_position = min_position
        elif line.startswith('L'):
            current_position -= 1
            if current_position < min_position:
                current_position = max_position
        if current_position == min_position:
            times_hit_min += 1
    print(f"New current position: {current_position}")

print(f"Times hit min position: {times_hit_min}")