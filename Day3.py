input_file = 'Day3_Input.csv'
# input_file = 'Day3_Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# Part 1
sum = 0
cur_val = 0
for line in lines:
    comp1 = line[:int(len(line) / 2)]
    comp2 = line[int(len(line) / 2):]
    for i in range(0, len(comp1)):
        if comp1[i] in comp2:
            if comp1[i] == comp1[i].lower():
                cur_val = ord(comp1[i]) - 96
            else:
                cur_val = ord(comp1[i]) - 38
    sum += cur_val
print("Part 1: " + str(sum))

# Part 2
sum = 0
cur_val = 0
for x in range(0, len(lines), 3):
    for i in range(0, len(lines[x])):
        if lines[x][i] in lines[x + 1] and lines[x][i] in lines[x + 2]:
            if lines[x][i] == lines[x][i].lower():
                cur_val = ord(lines[x][i]) - 96
            else:
                cur_val = ord(lines[x][i]) - 38
    sum += cur_val
print("Part 2: " + str(sum))