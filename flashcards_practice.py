f = open("state_capitals.txt", "r")

Match = {}
for line in f:
    result = line.strip().split(",")
    question = result[0]
    answer = result[1]
    Match[question] = answer

    print(Match)
