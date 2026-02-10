runs = []

for i in range(6):
    r = int(input("Enter run: "))
    runs.append(r)

total = 0
for r in runs:
    total = total + r

balls = len(runs)

if balls > 0:
    average = total / balls
    strike_rate = (total / balls) * 100
else:
    average = 0
    strike_rate = 0

print("Total runs:", total)
print("Average runs:", average)
print("Strike rate:", strike_rate)