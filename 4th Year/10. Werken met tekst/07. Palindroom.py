Word = input().lower()

def isPalindrome(Word):
    return Word == Word[::-1]

Palindrome = isPalindrome(Word)

if Palindrome:
    print('Dit is een palindroom')
else:
    print('Dit is geen palindroom')
