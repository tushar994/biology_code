dna = input("please give the dna sequence : \n")
print("\n\n\n")
dna = dna.lower()

# sequence = input("please give the RE's recognition sequence: \n")
# sequence = sequence.lower()

# ecoRI
# GAATTC

split_index = []

for i in range(0,len(dna)-5):
    copy = dna[i:i+6]
    if(copy=="gaattc"):
        print("g|",end="")
        split_index.append([i+1])
    else:
        print(dna[i],end="")
for i in range(len(dna)-5,len(dna)):
    print(dna[i],end="")

print("\n")
prev = 0
for val in split_index:
    print("ecoRI split at the index on W strand: "+str(val[0]))


for i,val in enumerate(split_index):
    print("fragment "+str(i+1)+" starts at "+str(prev+1) + " and ends at "+str(val[0])+".\nit's size is "+str(val[0]-prev))
    prev = val[0]
print("fragment "+str(len(split_index)+1)+" starts at "+str(prev+1) + " and ends at "+str(len(dna))+".\nit's size is "+str(len(dna)-prev))

# gtttcattataccagtttagaattctctatcgacagggcgttgagtgtgaattcgtgcttactcacggctgaattcggcatgtaggtaacagtagtggggaagcgtaacatctgaggcctgactcacatatagagt gtcgaccaaggggtgaagcatcatacgccatacaggcccctagcgaaacgacctagtcta aagacacacgagaatgaaacccgtggacttggttacagcgtaataatctggtcagagctg gtccggcgctggcgatgtaccttacgccactgcaaaccggctttgcagagaacatctggg tacattcccgtgtcatgtcaaagcaggtgattcccgcgaaaaacaattaacgacgcattt gctattgacgaagtcctagttctccgaattgagcgggagacatatgatgtcgagactgca ggaaccgaattatcctgtccgcagatccaatagctcacagaggtaaggggagtgtgatggtgccctagggtgtttgaacg