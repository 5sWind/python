Problem:

## C. Extraordinarily Nice Numbers

time limit per test:2 seconds
memory limit per test:256 megabytes
input:standard input
output:standard output
The positive integer a is a divisor of the positive integer b if and only if there exists a positive integer c such that a × c = b.

King Astyages thinks a positive integer x is extraordinarily nice if the number of its even divisors is equal to the number of its odd divisors.

For example 3 has two positive divisors 3 and 1, both of which are odd, so 3 is not extraordinarily nice. On the other hand 2 is only divisible by 2 and 1, so it has one odd and one even divisor. Therefore 2 is extraordinarily nice.

Given a positive integer x determine whether it's extraordinarily nice.

Input

> The input contains only a single integer x (1 ≤ x ≤ 103).

Output

> Write a single yes or no. Write yes if the number is extraordinarily nice and no otherwise.

> You don't need to care about capital or small letters. The output is case-insensitive.

Examples

input

> 2

output

> yes

input

> 3

output

> no

Keys:
```python
    def main():
        n = eval(input())
        odd = 0
        even = 0
        for i in range(1,n+1):
            if n%i == 0 and i%2 == 0:
                even += 1
            if n%i == 0 and i%2 != 0:
                odd += 1
        if even == odd:
            print("yes")
        else:
            print("no")
    
    if __name__ == '__main__':
        main()
```
