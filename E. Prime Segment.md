Problem:
## E. Prime Segment
time limit per test:2 seconds

memory limit per test:64 megabytes

input:standard input

output:standard output

Positive integer number x is called prime, if it has exactly two positive integer divisors. For example, 2, 3, 17, 97 are primes, but 1, 10, 120 are not.

You are given an integer number n, find the shortest segment [a, b], which contains n (i.e. a ≤ n ≤ b) and a, b are primes.

Input

> The only given line contains an integer number n (2 ≤ n ≤ 10000).

Output

> Print the space separated pair of the required numbers a, b.

Examples

input

> 10

output

> 7 11

input

> 97

output

> 97 97

Keys:
```
    def main():
    n = eval(input())
    pl = 1
    first, second = n, n
    if n%2 != 0 and n%3 != 0 and n%5 != 0:
        print(n,n)
    while first%2 == 0 or first%3 == 0 or first%5 == 0:
        first+=pl
        if first%2 != 0 and first%3 != 0 and first%5 != 0:
            break
    while second%2 == 0 or second%3 == 0 or second%5 == 0:
        second-=pl
        if second%2 != 0 and second%3 != 0 and second%5 != 0:
            break
    if n%2 == 0 or n%3 == 0 or n%5 == 0:
        print(second,first)

    if __name__ == '__main__':
        main()
```
