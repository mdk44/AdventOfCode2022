input_file = 'Day1_Input.csv'
# input_file = 'Day1_Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# Part 1
i = 0
cals = []
cals.append(0)
for x in range(0, len(lines)):
    if lines[x] == "":
        i += 1
        cals.append(0)
    else:
        cals[i] += int(lines[x])
print("Part 1: " + str(max(cals)))

# Part 2
top_three = 0
j = 0

while j < 3:
    top_three += max(cals)
    cals.remove(max(cals))
    j += 1

print("Part 2: " + str(top_three))

# adding comment to lazily fix the commit message