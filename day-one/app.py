import filereader

def get_number_from_line(line):
    return int(line.split()[1])

start_position = 50
min_position = 0
max_position = 99

lines = filereader.read_lines_from_file('input.txt')

for line in lines:
    if line.startswith('L'):
        start_position -= get_number_from_line(line)
    elif line.startswith('R'):
        start_position += get_number_from_line(line)