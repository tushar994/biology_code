import random

# Importing datetime.
from datetime import datetime

# Creating a datetime object so we can test.
a = datetime.now()

# Converting a to string in the desired format (YYYYMMDD) using strftime
# and then to int.
a = int(a.strftime('%Y%m%d%s'))
print(a)
random.seed(a)



length = input("please give length\n")

length = int(length)


genome = ""

i = 0
while ( i<length):
    a = random.randint(0,3)
    if(a==0):
        genome = genome + 'a'
    if(a==1):
        genome = genome + 't'
    if(a==2):
        genome = genome + 'g'
    if(a==3):
        genome = genome + 'c'
    a = random.randint(0,100)
    # if(a>=100):
    #     genome = genome + "gaattc"
    #     i+= 5
    i+=1

print(genome)