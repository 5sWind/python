Problem:
## I. Array sorting
time limit per test:2 seconds

memory limit per test:64 megabytes

input:standard input

output:standard output

Sorting arrays is traditionally associated with high-level languages. How hard can it be in Befunge? Sort the given array in non-descending order.

Input

> The first line of input contains an integer n (1 ≤ n ≤ 100) — the size of the array. The following n lines contain the elements of the array, one per line. Each element of the array is an integer between 1 and 60, inclusive. The array might contain duplicate elements.

Output

> Output space-separated elements of the sorted array.

Examples

input

> 5

> 7

> 1

> 9

> 7

> 3

output

> 1 3 7 7 9 

input

> 10

> 60

> 1

> 60

> 1

> 60

> 1

> 60

> 1

> 60

> 1


output

> 1 1 1 1 1 60 60 60 60 60 



Keys:
```
def main():
    m = eval(input())
    l = []
    for i in range(m):
        n = input()
        l.append(n)
    res = map(str,sorted(l))
    print(' '.join(res))

if __name__ == '__main__':
    main()
```
