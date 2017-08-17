Problem:
## A. Hexagonal numbers
> time limit per test:2 seconds

> memory limit per test:64 megabytes

> input:standard input

> output:standard output

> Hexagonal numbers are figurate numbers which can be calculated using the formula hn = 2n2 - n. You are given n; calculate n-th hexagonal number.

> Input

> The only line of input contains an integer n (1 ≤ n ≤ 100).

> Output

> Output the n-th hexagonal number.

> Examples

> input

> 2

> output

> 6

> input

> 5

> output

> 45


Keys:
```
def main():
    a = eval(input())
    b = 2*a*a-a
    print(b)


if __name__ == '__main__':
    main()
```
