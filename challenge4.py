def IsPalindrome(n):
    if len(n) == 1 or len(n) == 2 and n[0] == n[1]:
        return True
    elif n[0] == n[-1]:
        return IsPalindrome(n[1:-1])
    else:
        return False

for i in range(900, 999):
    for j in range(900, 999):
        if IsPalindrome(str(i * j)):
            print(str(i) + " * " + str(j) + " = " + str(i * j))
