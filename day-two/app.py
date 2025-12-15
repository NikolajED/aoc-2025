def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    lines_split = [line.split(',') for line in lines]
    return [item.strip() for sublist in lines_split for item in sublist]

ranges = read_lines_from_file('puzzle_input.txt')
print(ranges)
number_list = []
for r in ranges:
    print(r)
    start, end = map(int, r.split('-'))
    print(f"Start: {start}, End: {end}")
    lst = list(range(start, end + 1))
    for i in range(start, end + 1):
        str_i = str(i)
        if len(str_i) > 1 and all(ch == str_i[0] for ch in str_i):
            print(f"Adding number with same digit pattern: {i}")
            number_list.append(i)
        elif len(str_i) > 2:
            for i in range(2, 100):
                if len(str_i) % i == 0:
                    chunk_size = len(str_i) // i
                    chunk = str_i[:chunk_size]
                    if chunk * i == str_i:
                        print(f"Adding number with repeating pattern: {str_i}")
                        number_list.append(str_i)
                        break
                   
sum = 0
for n in number_list:
    sum += int(n)
print(sum)