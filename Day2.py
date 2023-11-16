input_file = 'Day2_Input.csv'
# input_file = 'Day2_Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# A = Rock
# B = Paper
# C = Scissors

# X = Rock, adds 1 point
# Y = Paper, adds 2 points
# Z = Scissors, adds 3 points

scores = {}
scores["A", "X"] = 4
scores["A", "Y"] = 8
scores["A", "Z"] = 3
scores["B", "X"] = 1
scores["B", "Y"] = 5
scores["B", "Z"] = 9
scores["C", "X"] = 7
scores["C", "Y"] = 2
scores["C", "Z"] = 6

total_score = 0
for line in lines:
    total_score += scores[line[0], line[2]]

print("Part 1: " + str(total_score))