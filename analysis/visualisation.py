import matplotlib.pyplot as plt

def load(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            try:
                data.append(int(line.strip()))
            except:
                pass
    return data

samples0 = load("data/0Rsamples.txt")
samples1 = load("data/1Rsamples.txt")
samples2 = load("data/2Rsamples.txt")

plt.figure(figsize=(10,6))

plt.hist(samples0, bins=50, alpha=0.5, label="0 resistors")
plt.hist(samples1, bins=50, alpha=0.5, label="1 resistor")
plt.hist(samples2, bins=50, alpha=0.5, label="2 resistors")

plt.xlabel("ADC Value")
plt.ylabel("Frequency")
plt.title("Comparison of ADC Distributions")
plt.legend()
plt.grid(True)

plt.show()