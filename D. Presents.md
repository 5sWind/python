Problem:
## D. Presents
time limit per test:2 seconds

memory limit per test:64 megabytes

input:standard input

output:standard output

You are given the prices of three presents. Also there are three sisters. It is known that the most valuable present is for the eldest sister. The second (by price) is for the second sister. And the less valuable present is for the youngest sister. If two (or three) presents have the same price, corresponding sisters may get the in a random way.

Input

> The only line contains three integer numbers a1, a2, a3 (1 ≤ a1, a2, a3 ≤ 100) — the prices of the presents.

Output

> Print three numbers i1, i2, i3 (1 ≤ i1, i2, i3 ≤ 3), all of them should be distinct. The first number stands for the seniority of the sister which will get the first present (1 stands for the eldest, 3 for the youngest). The second and third numbers mean the seniority of the sisters which get the second and the third present respectively.

> If there are multiple answers, print any of them.

Examples

input

> 11 13 1

output

> 2 1 3 

input

> 30 10 30

output

> 1 3 2 

Note

In the second sample another possible answer is "2 3 1".


Keys:
```
    def main():
        n = input().split()
        res = ['1', '2', '3']
        if n[0] > n[1]:
            if n[0] > n[2]:
                if n[1] >= n[2]:
                    print(' '.join(res))
                if n[2] > n[1]:
                    res[1], res[2] = res[2], res[1]
                    print(' '.join(res))
            if n[0] < n[2]:
                res[0], res[2] = res[2], res[0]
                res[2], res[1] = res[1], res[2]
                print(' '.join(res))
            if n[0] == n[2]:
                res[2], res[1] = res[1], res[2]
                print(' '.join(res))
            ''' Another answer
            if n[0] == n[2]:
                res[1], res[2] = res[2], res[1]
                res[0], res[2] = res[2], res[0]
                print(' '.join(res))
            '''
        if n[0] < n[1]:
            if n[0] >= n[2]:
                res[0], res[1] = res[1], res[0]
                print(' '.join(res))
            if n[0] < n[2]:
                if n[1] >= n[2]:
                    res[0], res[1] = res[1], res[0]
                    res[2], res[1] = res[1], res[2]
                    print(' '.join(res))
                if n[2] > n[1]:
                    res[0], res[2] = res[2], res[0]
                    print(' '.join(res))
            ''' Another answer
            if n[0] == n[2]:
                res[0], res[1] = res[1], res[0]
                res[0], res[2] = res[2], res[0]
                print(' '.join(res))
            '''
        if n[0] == n[1]:
            if n[0] >= n[2]:
                print(' '.join(res))
            if n[0] < n[2]:
                res[0], res[2] = res[2], res[0]
                res[2], res[1] = res[1], res[2]
                print(' '.join(res))

    if __name__ == '__main__':
        main()
```
