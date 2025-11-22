# entry = "AAAAGGCCT"

# # Count the letters in a string
# first= "A"
# second = "C"
# third = "G"
# fourth = "T"
# print(entry.count(first), entry.count(second), entry.count(third), entry.count(fourth))

# # Replace the letter in a string
# new_entry = entry.replace("T", "U")
# print(new_entry)

# # Reverse Compliment DNA
# def reverse_complement(sequence):
# # Define the complement mapping for DNA bases
#     complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
# # Generate the reverse complement
#     reversed_sequence = sequence[::-1]
#     reverse_complement = ''.join(complement[base] for base in reversed_sequence)
#
#     return reverse_complement
#
# # Example usage
# dna_sequence = ""
# print("Reverse Complement:", reverse_complement(dna_sequence))

# Hamming Distance Calculation

# def hamming_distance_calculation(str1, str2):
#     if len(str1) != len(str2):
#         print("Input must be of the same length")
#
#     distance = 0
#     for item in range(len(str1)):
#         if str1[item] != str2[item]:
#             distance += 1
#     return distance
#
#
# s = ""
# t = ""
# print(hamming_distance_calculation(s,t))

#Combing Through the Haystack
def finding_subset(str1, str2):
    if len(str2) > len(str1):
        print("Invalid input")
    location = []
    for i in range(len(str1)):
        point = str.find(str2[start:end])
        location.append(point)
        return location



s= "ATCGATAT"
t= "A"
print(finding_subset(s,t))