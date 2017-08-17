Problem:
## F. Prime factorization
time limit per test2 seconds

memory limit per test64 megabytes

inputstandard input

outputstandard output

You are given an integer n. Output its prime factorization.

If n = a1b1a2b2 ... akbk, where ak are prime numbers, the output of your program should look as follows: a1 a1 ... a1 a2 a2 ... a2 ... ak ak ... ak, where factors are ordered in non-decreasing order, and each factor ai is printed bi times.

Input

> The only line of input contains an integer n (2 ≤ n ≤ 250).

Output

> Output the prime factorization of n, as described above.

Examples

input

> 245

output

> 5 7 7 

input

> 13

output

> 13 


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
