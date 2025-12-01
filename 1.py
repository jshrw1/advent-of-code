start = 50
rgt = +1
lft = -1

with open("input.txt") as file:
    actions = [line.rstrip() for line in file]

list = []
for action in actions:
    if "R" in action:
        list.append(int(action.replace("R", "")) * rgt)
    elif "L" in action:
        list.append(int(action.replace("L", "")) * lft)


count = 0
passes = 0
for item in list:
    start = (start + item) % 100

    if start == 0:
        count += 1
print(count)


count = 0
passes = 0
for item in list:
    place = (start + item) % 100
    passes += abs((start + item) // 100)
    start = place
print(passes)
