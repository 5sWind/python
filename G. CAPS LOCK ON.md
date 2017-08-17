Problem:
## G. CAPS LOCK ON
time limit per test2 seconds

memory limit per test64 megabytes

inputstandard input

outputstandard output

You are given a string which consists of letters and other characters. Convert it to uppercase, i.e., replace all lowercase letters with corresponding uppercase ones. Keep the rest of characters unchanged.

Input

> The only line of input contains a string between 1 and 100 characters long. Each character of the string has ASCII-code between 33 (exclamation mark) and 126 (tilde), inclusive.

Output

> Output the given string, converted to uppercase.

Examples

input

> cOdEfOrCeS

output

> CODEFORCES

input

> ulr#4:befunge-RULES!

output

> ULR#4:BEFUNGE-RULES!


Keys:
```
def isprime(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            return False
            break
        else:
            count -= 1
    else:
        return True

def getfactors(num):
    l = []
    if isprime(num):
        return [num]
    count = num // 2
    for i in range(2, count + 1):
        if num % i == 0 and isprime(i):
             l.append(i)
    return l

def primecal(num):
    fac = getfactors(num)
    mul = 1
    for i in fac:
        mul *= i
    if mul == num:
        return fac
    else:
        return fac + primecal(num // mul)

if __name__ == '__main__':
    num = eval(input())
    res = map(str,sorted(primecal(num)))
    print(' '.join(res))
```
