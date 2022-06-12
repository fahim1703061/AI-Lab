def gcd(a, b):
    while (b):
        a, b = b, a % b

    return a

def lcm(num1, num2):
    gcd_val = gcd(num1, num2)
    lcm_val = (num1 * num2)/ gcd_val
    return lcm_val

num1= int( input("First number: "))
num2= int(input("second number: "))
lcm_val = lcm(num1, num2)

print(("lcm is ", lcm_val))
