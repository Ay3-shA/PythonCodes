#prime number checker


def prime_checker(number):
  if number % 2 == 1 and number % 3 != 0:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")




n = int(input("Check this numuber: "))
prime_checker(number = n)