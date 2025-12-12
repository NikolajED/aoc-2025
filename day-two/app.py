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
        s1 = str(i)
        # Found solution here https://www.geeksforgeeks.org/python/python-split-given-string-into-equal-halves/
        s2, s3 = s1[:len(s1)//2 + len(s1)%2], s1[len(s1)//2 + len(s1)%2:]
        if s2 == s3:
            print(f"Found palindrome: {i}")
            number_list.append(i)

sum = 0
for n in number_list:
    sum += n
print(sum)