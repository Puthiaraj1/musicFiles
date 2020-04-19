# text = "Welcome to Python Learning Program"
#
# capitals = [char.upper() for char in text]
#
# #print(capitals)
#
# words = [word.upper() for word in text.split(' ')]
#
# print(words)

# for x in range(1, 31):
#     fizzBuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
#     print(fizzBuzz)

fizzBuzz = [ "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz"
            if x % 5 == 0 else str(x) for x in range(1,31)]
print(fizzBuzz)

for buzz in fizzBuzz:
    print(buzz.center(12, '*'))