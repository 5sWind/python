Problem:

## G. Fibonacci army

time limit per test:2 seconds

memory limit per test:256 megabytes

input:standard input

output:standard output

King Cambyses loves Fibonacci numbers. He has several armies. Today he wants to make a new army for himself and he wants the number of men in this army to be the n-th Fibonacci number.

Given n you should find n-th Fibonacci number. The set of Fibonacci numbers start with f0 = f1 = 1 and for each i ≥ 2, fi = fi - 1 + fi - 2.

Input

> Input contains a single integer n (1 ≤ n ≤ 20).

Output

> Write a single integer. The n-th Fibonacci number.

Examples

input

> 2

output

> 2

input

> 1

output

> 1

Keys:
```python
    def main():
        num = ['1','1','2','3','5','8','13']
        n = input()
        if num[0] == n:
            print(''.join(num).find(n)+1)
        else:
            print(''.join(num).find(n))
    
    if __name__ == '__main__':
        main()
```
