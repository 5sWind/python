Problem:
## G. CAPS LOCK ON
time limit per test:2 seconds

memory limit per test:64 megabytes

input:standard input

output:standard output

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
def main():
    i = input()
    j = i.upper()
    print(j)

if __name__ == '__main__':
    main()
```
