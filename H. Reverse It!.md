Problem:
## H. Reverse It!
time limit per test:2 seconds

memory limit per test:64 megabytes

input:standard input

output:standard output

The 14th of March was the international day of mathematics, because of number π = 3.1415926...

In the occasion of this day Goofy Nephews Unity Organization (GNU) wants to publish the fastest program in math at 1:59:26 AM.

Now the time is 1:11:11 AM and the project team haven't checked their program yet. Because of shortage of time they want to check their program with some queries. So they hired Hormizd (one of the greatest programmers in world) to write a tester for GNU's new program. Because Hormizd has much more important things to do, he wants you to write a small part of tester and it is reversing the numbers. Help him before 1:59:26.

We can reverse numbers easily. For example by reversing 1234 we get 4321.

Note, that if the integer is negative then its reverse would be also negative. For example reverse of  - 123 is  - 321.

Also, you have to delete all the leading zeroes before and after the reverse.

Given an integer you have to help Hormizd reverse it.

Input

> The first line contains a single integer n. It is less than 101000 by it's absolute value. This integer may have leading zeros. If it had leading zeros you should first omit them and print the reverse of remaining digits. It's guaranteed that input contains less than 10001 characters.

Output

> Output a single integer, the reverse of the given number. You have to omit leading zeros in the output.

Examples

input

> 23

output

> 32

input

> -032

output

> -23

input

> 01234560

output

> 654321


Keys:
```
    import re

    def main():
        n = input()
        m = list(n)
        for i in range(len(m)):
            if m[0] == '0' or m[1] == '0' or m[-1] == '0':
                m.remove('0')
        m.reverse()
        j = ''.join(m)
        rec = r'\-'
        if re.match(rec ,n):
            i = j.find('-')
            k = j.replace('-','')
            o = j[i] + k
            print(o)
        else:
            print(j)
    
    if __name__ == '__main__':
        main()
```
