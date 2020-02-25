# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


first pass: single loop, input size is O of n to the power of some constant
second pass: This is obfuscation. 
while a < n^3 (affects runtime, number of loops) **
a equals a + n^2 (does not affect runtime, it's the same operation no matter what)

```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
double loop, as input increases you repeat the subloop over the same stuff. This is literally the bubblesort algo pattern. Must also be input size of O of n to the power of 2.

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
Recursion, but it obfuscates that this is just adding the number 2 over and over. The number of additions of 2 (operations) is directly proportional to the input size, so this is constant time.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
