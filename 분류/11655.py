s = input()
result = ""

for i in range(len(s)):
    char = s[i]
    if char.isupper():
        result += chr((ord(char) + 13 - 65) % 26 + 65)
    elif char.islower():
        result += chr((ord(char) + 13 - 97) % 26 + 97)
    else:
        result += char

print(result)