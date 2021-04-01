dna = input("please give the dna sequence : \n")

dna = dna.lower()

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
for val in split_index:
    print("ecoRI split at the index : "+str(val[0]))


# gtttcattataccagtttagaattctctatcgacagggcgttgagtgtgaattcgtgcttactcacggctgaattcggcatgtaggtaacagtagtggggaagcgtaacatctgaggcctgactcacatatagagt gtcgaccaaggggtgaagcatcatacgccatacaggcccctagcgaaacgacctagtcta aagacacacgagaatgaaacccgtggacttggttacagcgtaataatctggtcagagctg gtccggcgctggcgatgtaccttacgccactgcaaaccggctttgcagagaacatctggg tacattcccgtgtcatgtcaaagcaggtgattcccgcgaaaaacaattaacgacgcattt gctattgacgaagtcctagttctccgaattgagcgggagacatatgatgtcgagactgca ggaaccgaattatcctgtccgcagatccaatagctcacagaggtaaggggagtgtgatggtgccctagggtgtttgaacg