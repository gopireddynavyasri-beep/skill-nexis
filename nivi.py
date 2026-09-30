num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Prime Number
if num <= 1:
    print(num, "is not a Prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num, "is a Prime number")
    else:
        print(num, "is not a Prime number")