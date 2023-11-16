input_file = 'Day2_Input.csv'
# input_file = 'Day2_Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

# Part 1

# A = Rock, B = Paper, C = Scissors
# X = Rock, adds 1 point; Y = Paper, adds 2 points; Z = Scissors, adds 3 points
# Lose = 0 points, Draw = 3 points, Win = 6 points
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

# Part 2

# ABC same as above
# X = lose, Y = draw, Z = win, my choice adds same points as above
# Same win points as above
scores = {}
scores["A", "X"] = 3
scores["A", "Y"] = 4
scores["A", "Z"] = 8
scores["B", "X"] = 1
scores["B", "Y"] = 5
scores["B", "Z"] = 9
scores["C", "X"] = 2
scores["C", "Y"] = 6
scores["C", "Z"] = 7

total_score = 0
for line in lines:
    total_score += scores[line[0], line[2]]

print("Part 2: " + str(total_score))