# biology_code

This is a repo containing code that does what is asked in the question pdf `Prog_Assignment_1.pdf`

## Q1
1. Write a code to accept any DNA sequence (of varying lengths) and produce as output the corresponding RNA strand synthesized and protein strand synthesized.

This is a standard proceedure. 
- First we find the complement of the DNA strand. This is done by switching out the a's for t's, t's for a's, g's for c's and c's for g's.
- Then we take this new string and change all the a's to u's, t's to a's, c's to g's and g's to c's. This third string is the mRNA strand.
- Then we find the tRNA strand by finding the compliment of the mRNA strand.
- Then we find the protein strand from the mRNA strand by taking the mRNA strand three letters at a time and mapping them to their respective protein name.


## Q2
2. Write a program to generate a restriction map for a specific RE and compare your results with Mapper. Give the RE and the genomic sequence used.

I chose ecoRI as my RE. This one splits on GAATTC. So, i simply find all occurances of this substring in the main string, and make cuts in those places. Read the report in `./question2/Report.md` for more information.

## Q3
3. Write a program to identify restriction recognition sites in a given DNA sequence. 

This is easy. We simply find all occurances of complimentary palidromes of lengths 4,6,8. These are all the restriction sites in the DNA sequence.
