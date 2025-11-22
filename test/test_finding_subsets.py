import pytest

from finding_subset import finding_subset


def test_empty_strings():
    assert finding_subset("", "") == []

def test_single_char_single_instance():
    assert finding_subset("agtcac", "t") == [2]

def test_single_char_multiple_instances():
    assert finding_subset("agtcactcaca", "a") == [0, 4, 8, 10]

def test_multi_char_single_instance():
    assert finding_subset("agtcactca", "cac") == [3]

def test_multi_char_multiple_instance():
    assert finding_subset("agcatcactca", "ca") == [2, 5, 9]

def test_len_throws_exception():
    with pytest.raises(ValueError, match="Invalid input"):
        finding_subset("agtc", "agcgtc")

