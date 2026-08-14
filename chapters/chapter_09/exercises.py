## EXERCISES

# 2. Exercise
print("\nEXERCISE 2")
def is_anagram(text1: str, text2: str) -> bool:
    sort1: str = ''.join(sorted(text1))
    sort2: str = ''.join(sorted(text2))
    return sort1 == sort2
print("done")


# 3. Exercise
print("\nEXERCISE 3")
def reverse_word(word: str) -> str:
    return ''.join(reversed(word))
def is_palindrome(text: str) -> bool:
    return reverse_word(text) == text
print("done")


# 4. Exercise
print("\nEXERCISE 4")
def reverse_sentence(text: str) -> str:
    return (' '.join(reversed(text.split()))).capitalize()
print(reverse_sentence('Reverse this sentence'))


# 5. Exercise
print("\nEXERCISE 5")
string = open('data/words.txt').read()
word_list = string.split()
def total_length(list_of_str: list) -> int:
    total: int = 0
    for word in list_of_str:
        total += len(word)
    return total
print(total_length(word_list))   # 902728