"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError("No <= 0 values.")
    list = []
    first = 2
    while len(list) < number_of_primes:
        pcheck = [first for i in list if first%i == 0]
        list += [] if pcheck else [first]
        first += 1
    return list