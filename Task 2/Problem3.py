
pattern = "AAAACCCGGT"

complement = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
    
}
reverse_complement = ""
for nucleotide in pattern[::-1]:
    reverse_complement += complement[nucleotide]
    
print(reverse_complement)
