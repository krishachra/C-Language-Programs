def is_anagram(str1, str2):
    """
    Returns True if str1 and str2 are anagrams, False otherwise.
    """
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

# User input
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if is_anagram(s1, s2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Test cases
assert is_anagram("listen", "silent") == True
assert is_anagram("hello", "world") == False
assert is_anagram("Dormitory", "Dirty room") == True
