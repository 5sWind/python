Problem:

## B. New Year and North Pole

time limit per test:2 seconds

memory limit per test:256 megabytes

input:standard input

output:standard output

In this problem we assume the Earth to be a completely round ball and its surface a perfect sphere. The length of the equator and any meridian is considered to be exactly 40 000 kilometers. Thus, travelling from North Pole to South Pole or vice versa takes exactly 20 000 kilometers.

Limak, a polar bear, lives on the North Pole. Close to the New Year, he helps somebody with delivering packages all around the world. Instead of coordinates of places to visit, Limak got a description how he should move, assuming that he starts from the North Pole. The description consists of n parts. In the i-th part of his journey, Limak should move ti kilometers in the direction represented by a string diri that is one of: "North", "South", "West", "East".

Limak isn’t sure whether the description is valid. You must help him to check the following conditions:

* If at any moment of time (before any of the instructions or while performing one of them) Limak is on the North Pole, he can move only to the South.
* If at any moment of time (before any of the instructions or while performing one of them) Limak is on the South Pole, he can move only to the North.
* The journey must end on the North Pole.

Check if the above conditions are satisfied and print "YES" or "NO" on a single line.

Input

> The first line of the input contains a single integer n (1 ≤ n ≤ 50).

> The i-th of next n lines contains an integer ti and a string diri (1 ≤ ti ≤ 106, ) — the length and the direction of the i-th part of the journey, according to the description Limak got.

Output

> Print "YES" if the description satisfies the three conditions, otherwise print "NO", both without the quotes.

Examples

input

> 5

> 7500 South

> 10000 East

> 3500 North

> 4444 West

> 4000 North

output

> YES

input

> 2

> 15000 South

> 4000 East

output

> NO

input

> 5

> 20000 South

> 1000 North

> 1000000 West

> 9000 North

> 10000 North

output

> YES

input

> 3

> 20000 South

> 10 East

> 20000 North

output

> NO

input

> 2

> 1000 North

> 1000 South

output

> NO

input

> 4

> 50 South

> 50 North

> 15000 South

> 15000 North

output

> YES

Note

Drawings below show how Limak's journey would look like in first two samples. In the second sample the answer is "NO" because he doesn't end on the North Pole.

[image](http://codeforces.com/predownloaded/b2/24/b224619452c99ddf47f15b867801f4191978aa1c.png)

Keys:
```python
    def main():
        n = eval(input())
        count = 0
        license = False
        for i in range(n):
            m = input().split()
            if i == 0:
                if m[1].find('South') != -1:
                    license = True
            if ''.join(m).find('North') != -1:
                count += 1
        if license and m[-1].find('North') != -1 and count >= 2:
            print("YES")
        else:
            print("NO")
    
    if __name__ == '__main__':
        main()
```
