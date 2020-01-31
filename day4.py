def increasing(digits):
    for i in range(0, len(digits)-1):
        if int(digits[i]) > int(digits[i+1]):
            return False
    return True

def adjacentSame(chars):
    for i in range(0, len(chars)-1):
        if chars[i] == chars[i+1]:
            return True
    return False

matching = 0
for i in range(137683, 596253+1):
    if increasing(str(i)) and adjacentSame(str(i)):
        matching += 1

print(matching)
