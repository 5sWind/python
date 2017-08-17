Problem:
## B. Gnikool Ssalg
time limit per test:2 seconds

memory limit per test:64 megabytes

input:standard input

outputstandard output

You are given a string. Reverse its characters.

Input

> The only line of input contains a string between 1 and 100 characters long. Each character of the string has ASCII-code between 33 (exclamation mark) and 126 (tilde), inclusive.

Output

> Output the characters of this string in reverse order.

Examples

input

> secrofedoc

output

> codeforces

input

> !ssalg-gnikool5

output

> 5looking-glass!


Keys:
```
def main():
    string = input()
    print(string[::-1])

if __name__ == '__main__':
    main()
```
