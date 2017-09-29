Problem:

## E. New Year and Old Subsequence

time limit per test:2 seconds

memory limit per test:256 megabytes

input:standard input

output:standard output

A string t is called nice if a string "2017" occurs in t as a subsequence but a string "2016" doesn't occur in t as a subsequence. For example, strings "203434107" and "9220617" are nice, while strings "20016", "1234" and "20167" aren't nice.

The ugliness of a string is the minimum possible number of characters to remove, in order to obtain a nice string. If it's impossible to make a string nice by removing characters, its ugliness is  - 1.

Limak has a string s of length n, with characters indexed 1 through n. He asks you q queries. In the i-th query you should compute and print the ugliness of a substring (continuous subsequence) of s starting at the index ai and ending at the index bi (inclusive).

Input

> The first line of the input contains two integers n and q (4 ≤ n ≤ 200 000, 1 ≤ q ≤ 200 000) — the length of the string s and the number of queries respectively.

> The second line contains a string s of length n. Every character is one of digits '0'–'9'.

> The i-th of next q lines contains two integers ai and bi (1 ≤ ai ≤ bi ≤ n), describing a substring in the i-th query.

Output

> For each query print the ugliness of the given substring.

Examples

input

> 8 3

> 20166766

> 1 8

> 1 7

> 2 8

output

> 4

> 3

> -1

input

> 15 5

> 012016662091670

> 3 4

> 1 14

> 4 15

> 1 13

> 10 15

output

> -1

> 2

> 1

> -1

> -1

input

> 4 2

> 1234

> 2 4

> 1 2

output

> -1

> -1

Note
In the first sample:

In the first query, ugliness("20166766") = 4 because all four sixes must be removed.
In the second query, ugliness("2016676") = 3 because all three sixes must be removed.
In the third query, ugliness("0166766") =  - 1 because it's impossible to remove some digits to get a nice string.
In the second sample:

In the second query, ugliness("01201666209167") = 2. It's optimal to remove the first digit '2' and the last digit '6', what gives a string "010166620917", which is nice.
In the third query, ugliness("016662091670") = 1. It's optimal to remove the last digit '6', what gives a nice string "01666209170".


Keys:
```python
    def main():
        n = input().split()
        s = input()
        count = 0
        for j in range(eval(n[1])):
            m = input().split()
            a = eval(m[0])-1
            b = eval(m[1])
            str = s[a:b]
            cat = str[str.find('7') + 1:]
            nplus = str[str.find('2'):str.find('7')+1]
            for i in range(len(str)):
                if str.find('2016') != -1 and str[str.find('2016')+1:].find('2') != -1:
                    str = str[:str.find('2016')] + str[str.find('2016')+1:]
                    count += 1
                    nplus = str[str.find('2'):str.find('7')+1]
                if nplus.find('6') != -1:
                    nplus = nplus[:nplus.find('6')] + nplus[nplus.find('6')+1:]
                    count += 1
                if cat.find('6') != -1:
                    cat = cat[:cat.find('6')] + cat[cat.find('6')+1:]
                    count += 1
            if str.find('2') == -1 or str.find('0') == -1 or str.find('1') == -1 or str.find('7') == -1:
                print(-1)
            else:
                print(count)
            count = 0
    
    if __name__ == '__main__':
        main()
```
