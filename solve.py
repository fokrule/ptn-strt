l1 = [2,4,3]
l2 = [5,6,4]
output = []
reminder = 0
for index in range(0, len(l1)):
    if ((l1[index] + l2[index]) // 10 != 0):
        reminder = (l1[index] + l2[index]) // 10
    output.append((reminder + l1[index] + l2[index]) %10)
print(output[::-1])