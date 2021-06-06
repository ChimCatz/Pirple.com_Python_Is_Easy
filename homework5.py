# Homework#5

lower = 2
upper = 100

print(1)
for num in range(lower, upper + 1):
    flag = 0
    for div in range(2, num):
        if num % div == 0:
            flag = 1

    if flag == 0:
        print("prime")

    else:
        if num % 15 == 0:
            print("FizzBuzz")
            continue
        if num % 3 == 0:
            print("Fizz")
            continue
        if num % 5 == 0:
            print("Buzz")
            continue

        else:
            print(num)