def gcd(a, b):
    while (b):
        a, b = b, a % b

    return a


value = gcd(15, 10)

print("gcd is", value)