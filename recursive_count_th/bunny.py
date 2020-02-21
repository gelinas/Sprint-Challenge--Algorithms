def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)

print(bunnyEars(1))

print(bunnyEars(2))

print(bunnyEars(3))

print(bunnyEars(4))

print(bunnyEars(5))

print(bunnyEars(10))

print(bunnyEars(100))

# print(bunnyEars(10000))

# print(bunnyEars(10000000))

# print(bunnyEars(1000000000000))