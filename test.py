sample = dict()

with open("test.txt", "r") as a_file:
    for line in a_file:
        for word in line.split():
            if word in sample:
                sample[word] = sample[word] + 1
            else:
                sample[word] = 1

print(sample)