# input_file = 'Day2_Input.csv'
input_file = 'Day2_Test.csv'
text_file = open(input_file)
lines = text_file.read().split('\n')

for line in lines:
    print(line)
