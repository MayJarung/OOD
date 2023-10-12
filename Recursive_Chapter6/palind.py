def isPalind(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return isPalind(word[1:-1])

inp = input("Enter Input : ")
if isPalind(inp):
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp}' is not palindrome")