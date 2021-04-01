dna = input("please give the dna sequence : \n")

dna = dna.lower()

reverse = ""

for char in dna:
    if(char=='a'):
        reverse = reverse + 't'
    elif(char=='t'):
        reverse = reverse + 'a'
    elif(char=='g'):
        reverse = reverse + 'c'
    elif(char=='c'):
        reverse = reverse + 'g'

print("reverse is :" + reverse)

mRNA = ""
# a->u, t->a, c<->g
for char in reverse:
    if(char=='a'):
        mRNA = mRNA + 'u'
    elif(char=='t'):
        mRNA = mRNA + 'a'
    elif(char=='g'):
        mRNA = mRNA + 'c'
    elif(char=='c'):
        mRNA = mRNA + 'g'

print("mRNA is :" + mRNA)

tRNA = ""
# a<->u, g<->c
for char in mRNA:
    if(char=='a'):
        tRNA = tRNA + 'u'
    elif(char=='u'):
        tRNA = tRNA + 'a'
    elif(char=='g'):
        tRNA = tRNA + 'c'
    elif(char=='c'):
        tRNA = tRNA + 'g'

print("tRNA is :" + tRNA)


protein = []

print("okay")

start_flag = 0
for i in range(0, len(mRNA), 3):
    # print(i)
    three = mRNA[i:i+3]
    if(three[0]=='u'):
        if(start_flag==1):
            if(three[1]=='u'):
                if(three[2]=='u' or three[2]=='c'):
                    protein.append("phe")
                else:
                    protein.append("leu")
            elif(three[1]=='c'):
                protein.append("ser")
            elif(three[1]=='a'):
                if(three[2]=='u' or three[2]=='c'):
                    protein.append("tyr")
                else:
                    protein.append("STOP")
                    break
            else:
                if(three[2]=='u' or three[2]=='c'):
                    protein.append("cys")
                elif(three[2]=='a'):
                    protein.append("STOP")
                    break
                else:
                    protein.append("trp")
    
    elif(three[0]=='c'):
        if(start_flag==1):
            if(three[1]=='u'):
                protein.append("leu")
            elif(three[1]=='c'):
                protein.append("pro")
            elif(three[1]=='g'):
                protein.append("arg")
            else:
                if(three[2]=='u' or three[2]=='c'):
                    protein.append("his")
                else:
                    protein.append("gln")
    
    elif(three[0]=='a'):
        if(three[1]=='u'):
            if(three[2]=='g'):
                protein.append("met")
                start_flag = 1
            else:
                if(start_flag==1):
                    protein.append("ile")
        elif(three[1]=='c'):
            if(start_flag==1):
                protein.append("thr")
        elif(three[1]=='a'):
            if(start_flag==1):
                if(three[2]=='u' or three[2]=='c'):
                    protein.append("asn")
                else:
                    protein.append("lys")
        else:
            if(start_flag==1):
                if(three[2]=='u' or three[2]=='c'):
                    protein.append("ser")
                else:
                    protein.append("arg")
    else:
        if(start_flag==1):
            if(three[1]=='u'):
                protein.append("val")
            elif(three[1]=='c'):
                protein.append("ala")
            elif(three[1]=='a'):
                if(three[2]=='u' or three[2]=='c'):
                    protein.append("asp")
                else:
                    protein.append("glu")
            else:
                protein.append("gly")


if(start_flag==0):
    print("no start colon found")
else:
    for element in protein:
        print(element, end=" ")

print("\n")