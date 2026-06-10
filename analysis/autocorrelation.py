samples = []

with open("data/2Rsamples.txt") as f:
    for line in f:
        try:
            samples.append(int(line))
        except:
            pass

zeros = 0
ones = 0
numbers = []

for x in samples:
    bit = x & 1

    if bit == 0:
        zeros += 1
        numbers.append(0)
        
    else:
        ones += 1
        numbers.append(1)
        

output = []

for bit in range(0, len(numbers) - 1, 2):
    a = numbers[bit]
    b = numbers[bit + 1]

    if a == 0 and b == 1:
        output.append(0)

    elif a == 1 and b == 0:
        output.append(1)

z = o = 0
for i in output:
    if i == 0: z += 1
    else: o += 1

print()
print("".join(str(bit) for bit in output))
print()
print("Zeros:", zeros)
print("Ones :", ones)

print("Percentage of zeros:", zeros / (zeros + ones))
print("Percentage of ones :", ones / (zeros + ones))

print ("Percentage of zeros in output:", z / (z + o))
print ("Percentage of ones in output :", o / (z + o))