from reverse_complement import reverse_complement

def test_reverse_complement():
    assert reverse_complement(A) == T
    assert reverse_complement(T) == A
    assert reverse_complement(G) == C
    assert reverse_complement(C) == G
    assert reverse_complement("AGTC") == "GACT"
    assert reverse_complement("") == ""