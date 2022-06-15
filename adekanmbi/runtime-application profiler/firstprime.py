def firstPrimeAfter(x):
        import math
        current = x + 1
        sqrtno = math.sqrt(current)
        while True:
                #search for primes starting at x until it finds one
                #break once found a prime
                for potentialfactor in range(2,current):
                        # start at 2 because 1 will always be a factor
                        # go all the way up to the sqrt of current looking for a factor
                        if current % potentialfactor == 0:
                                # Found factor. not prime
                                break # move on to next number
                        elif potentialfactor >= sqrtno:
                                #print("The first prime number after {} is {}".format(x,current))
                                return current
                current += 1

for i in range(10000000):
    firstPrimeAfter(i)
