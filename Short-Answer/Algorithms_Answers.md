#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Quadratic runtime. single loop, but the cap of that loop is exponentially related to input size. runtime is O of n to the power of some constant (3 in this case). This is quadratic runtime.


b) Quadratic runtime. double loop, as input increases you repeat the subloop over the same stuff. This is literally the bubblesort algo pattern. Must also be input size of O of n to the power of 2. Also quadratic runtime.


c) Constant runtime. Recursion, but the recursion formula obfuscates that this is just adding the number 2 over and over. The number of additions of 2 (operations) is directly proportional to the input size, so this is constant time.

## Exercise II

This should be a binary search, and I'd pick the midpoint first. Drop off the middle, if it breaks move halfway down, if it doesn't break move halfway up. Keep dividing until you can't move anymore. 

If your last test broke the egg, floor 'f' (the maximum floor) is n
If your last test didn't break the egg, floor 'f' (the maximum floor) is n+1.

At this point you've found the exact floor it breaks.

This equation will have logarithmic runtime (like searching the dictionary)