from functools import lru_cache

@lru_cache(maxsize=None)
def antipalindrome(word: str):
    if (len(word) == 1):
        return 0
    elif word != word[::-1]:
        return len(word)
    elif word == word[::-1]:
        return antipalindrome(word[:-1])


print(antipalindrome("gggggggg"))
print(antipalindrome("anna"))
print(antipalindrome("wuffuw"))
print(antipalindrome("mew"))
