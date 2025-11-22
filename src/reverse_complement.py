A = "A"
T = "T"
G = "G"
C = "C"

# Reverse Compliment DNA
def reverse_complement(sequence):
    # Define the complement mapping for DNA bases
    complement = {A: T, T: A, C: G, G: C}
    # Generate the reverse complement
    reversed_sequence = sequence[::-1]
    rev_comp = "".join(complement[base] for base in reversed_sequence)

    return rev_comp

if __name__ == "__main__":
    dna_sequence = "TAGC"
    print("Reverse Complement:", reverse_complement(dna_sequence))


def test_reverse_complement():
    assert reverse_complement(A) == T
    assert reverse_complement(T) == A
    assert reverse_complement(G) == C
    assert reverse_complement(C) == G
    assert reverse_complement("AGTC") == "GACT"
    assert reverse_complement("") == ""