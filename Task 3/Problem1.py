
Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4
d = 1
from itertools import product

def diff(a,b):
    return sum (a[i] !=b[i] for i in range(len(a)))
    
max_count =0
result = []
    
for p in product("ACGT", repeat=k):
        pattern = "".join(p)
        count = 0
        
        for i in range (len(Text) - k +1):
            if diff(pattern, Text[i:i+k]) <= d:
                count += 1
                
                if count >max_count:
                    max_count=count
                    result = [pattern]
                elif count == max_count:
                        result.append(pattern)
print(" ".join(result))
                        
