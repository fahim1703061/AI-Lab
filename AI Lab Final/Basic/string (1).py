str1 = "GATTACA"

# print(str1[1:3])
# print(str1[:2])
# print(str1[:3])
# print(str1[3:5])
# print(str1[-1])
# print(str1[-2])
# print(str1[-4:-1])

# print(str1.find("TAC"))
# #print(len(str1))

# print("TAC" in str1)

# print("38" + str(5))

# print(str1.lower())

# print(str1.replace('GATTACA','Pyhton')) #will create copy of a original string

# print(str1.startswith('G')) #case sensitive
# print(str1.endswith('A'))

# print(str1.find('Gat')) #didn't find the substring, case sensitive

# print(str1.islower()) #checks if everything is in lower case

# print(str1.count('A')) #counts the number of occurance of given substring

# seq = input("Enter a string: ")
# sub_seq = input("Enter a substring: ")

# print("\nSubstring is in main sequence: ", sub_seq in seq)
# print("'ATA' is in main sequence: ", 'ATA' in seq)
# print("Number of A is in main sequence: ", seq.count('A'))
# print("There are ", seq.count('T'), ' number of T')

dna_seq = input("Enter a dna sequence: ")
print("It is", len(dna_seq), "bases long")
print("Adenine:", (dna_seq.upper()).count('A'))
print("Thyamine:", (dna_seq.upper()).count('T'))
print("Cytonine:", (dna_seq.upper()).count('C'))
print("Guanine:", (dna_seq.upper()).count('G'))

number_of_bases = (dna_seq.upper()).count('A') + (dna_seq.upper()).count('T') + (dna_seq.upper()).count('C') + (dna_seq.upper()).count('G')

if len(dna_seq)-number_of_bases > 0:
    print('Unknown:', len(dna_seq)-number_of_bases)






