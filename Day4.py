input_file = 'Day4_Input.csv'
# input_file = 'Day4_Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

def parse_line(inp):
    ser1 = inp.split(',')[0]
    ser2 = inp.split(',')[1]
    num11 = int(ser1.split('-')[0])
    num12 = int(ser1.split('-')[1])
    num21 = int(ser2.split('-')[0])
    num22 = int(ser2.split('-')[1])
    return num11, num12, num21, num22

# Part 1
sum = 0
for line in lines:
    x1, x2, y1, y2 = parse_line(line)
    if x1 >= y1 and x2 <= y2:
        sum += 1
    elif x1 <= y1 and x2 >= y2:
        sum += 1

print("Part 1: " + str(sum))