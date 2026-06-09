
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4   
count = {}

for i in range(len(text) - k + 1):
    pattern = text[i:i + k]
    if pattern in count:
        count[pattern] += 1
    else:
        count[pattern] = 1
max_count = max(count.values())

for pattern in count:
    if count[pattern] == max_count:
        print(pattern, end=" ")
